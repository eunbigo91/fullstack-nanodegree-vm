#
# Database access functions for the web forum.
#

import psycopg2
import bleach

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    #posts = [{'content': str(row[1]), 'time': str(row[0])} for row in DB]
    #posts.sort(key=lambda row: row['time'], reverse=True)
    conn = psycopg2.connect("dbname=forum")
    cursor = conn.cursor()
    cursor.execute("select time, content from posts order by time desc")
    posts = [{'content': str(row[1]), 'time': str(row[0])} for row in cursor.fetchall()]
    conn.close()
    return posts

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    conn = psycopg2.connect("dbname=forum")
    cursor = conn.cursor()
    cursor.execute("insert into posts (content) values (%s)", (content,))
    conn.commit()
    conn.close()

