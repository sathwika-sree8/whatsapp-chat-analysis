import streamlit as st
from scipy.spatial.transform import Rotation
from streamlit import sidebar

import preprocessor,helper
import matplotlib.pyplot as plt
import seaborn as sns
st.sidebar.title("whatsapp chat analyser")

uploaded_file = st.sidebar.file_uploader("Choose a file",key="file_uploader_1")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")
    df=preprocessor.preprocess(data)

    user_list=df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user=st.sidebar.selectbox("Chat analysis",user_list)
    num_messages = 0
    words=[]
    num_media_messages=0
    num_links=0
    if st.sidebar.button("Show analysis"):
        num_messages,words,num_media_messages,num_links= helper.fetch_stats(selected_user, df)
    st.title("Top Statistics")
    col1,col2,col3,col4= st.columns(4)
    with col1:
        st.header("Total Messages")
        st.title(num_messages)

    with col2:
        st.header("Total Words")
        st.title(len(words))
    with col3:
        st.header("Total Media shared")
        st.title(num_media_messages)
    with col4:
        st.header("Total Links shared")
        st.title(num_links)

    st.title("Monthly timeline")
    timeline=helper.monthly_timeline(selected_user,df)
    fig,ax=plt.subplots()
    ax.plot(timeline['time'], timeline['message'])
    plt.xticks(rotation='vertical')
    st.pyplot(fig)
    st.title("Daily timeline")
    daily_timeline = helper.daily_timeline(selected_user, df)
    fig, ax = plt.subplots()
    ax.plot(daily_timeline['only_date'], daily_timeline['message'],color='green')
    plt.xticks(rotation='vertical')
    st.pyplot(fig)

    st.title('Activity Map')
    cal1,col2=st.columns(2)
    with col1:
        st.header("Most busy day")
        busy_day=helper.week_activity_map(selected_user,df)
        fig,ax=plt.subplots()
        ax.bar(busy_day.index,busy_day.values)
        st.pyplot(fig)
    with col2:
        st.header("Most busy month")
        busy_month=helper.month_activity_map(selected_user,df)
        fig,ax=plt.subplots()
        ax.bar(busy_month.index,busy_month.values,color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user, df)
        fig,ax = plt.subplots()
        sns.heatmap(user_heatmap, ax=ax, cmap="magma", annot=True)
        st.pyplot(fig)


    if selected_user=='Overall':
        st.title('Most busy users')
        x,new_df=helper.most_busy_users(df)
        fig , ax=plt.subplots()
        ax.bar(x.index,x.values)
        ax.bar(x.index, x.values, color='red')
        ax.set_xticklabels(x.index, rotation=90, ha='right', color='black')

        st.pyplot(fig)
        col1,col2= st.columns(2)

        with col1:
            ax.bar(x.index, x.values)
            plt.xticks(rotation='vertical',color='red')
            st.pyplot(fig)
        with col2:
            st.dataframe(new_df)
    st.title("Wordcloud")
    df_wc=helper.create_wordcloud(selected_user,df)
    fig,ax=plt.subplots()
    ax.imshow(df_wc)
    st.pyplot(fig)

    most_common_df=helper.most_common_words(selected_user,df)
    fig,ax=plt.subplots()
    ax.barh(most_common_df[0],most_common_df[1])
    plt.xticks(rotation='vertical')
    st.title('Most common words')
    st.pyplot(fig)
    st.dataframe(most_common_df)
    #emoji
    emoji_df=helper.emoji_helper(selected_user,df)
    st.title("Emoji Analysis")
    st.dataframe(emoji_df)
    col1,col2=st.columns(2)

    with col1:
        st.dataframe(emoji_df)
    with col2:
        fig,ax=plt.subplots()
        ax.pie(emoji_df[1].head(),labels=emoji_df[0].head(),autopct="%0.2f")
        st.pyplot(fig)
