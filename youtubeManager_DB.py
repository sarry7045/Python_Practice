import sqlite3

connection = sqlite3.connect("youtube_videos.db")

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')


def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?,?)", (name, time))
    connection.commit()

def update_video(video_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    connection.commit()

def delete_video(vidoe_id):
    cursor.execute("DELETE FROM videos where id = ?", (vidoe_id,))
    connection.commit()


def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Vidoes")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")
        choice = input("Enter your Choice")

        if choice == "1":
            list_videos()
        elif choice == "2":
           name = input("Enter the video name: ")
           time = input("Enter the video time: ")
           add_video(name, time)
        elif choice == "3":
           video_id = input("Enter video ID to Update: ")
           name = input("Enter the video name: ")
           time = input("Enter the video time: ")
           update_video(video_id, name, time)
        elif choice == "4":
           video_id = input("Enter video ID to Delete: ")
           delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid Choice: ")

    connection.close()



if __name__ == "__main__":
    main()