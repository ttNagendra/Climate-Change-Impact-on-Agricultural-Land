import streamlit as st
import sqlite3
import base64

st.markdown(f'<h1 style="color:#8d1b92;text-align: center;font-size:36px;">{"Climate Change Impact on Agricultural Land"}</h1>', unsafe_allow_html=True)


st.write("---------------------------------------------------------------------------------")

st.markdown(f'<h1 style="color:#000000;font-size:24px;text-align:center;font-family:canvat;">{"Login Here !!!"}</h1>', unsafe_allow_html=True)



def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('2.jpg')



# Function to create a database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn

# Function to create a new user
def create_user(conn, user):
    sql = ''' INSERT INTO users(name, password, email, phone)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid

# Function to validate user credentials
def validate_user(conn, name, password):
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name=? AND password=?", (name, password))
    user = cur.fetchone()
    if user:
        return True, user[1]  # Return True and user name
    return False, None

# Main function
def main():
    # st.title("User Login")
    # st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:24px;">{"Login here"}</h1>', unsafe_allow_html=True)


    # Create a database connection
    conn = create_connection("dbs.db")

    if conn is not None:
        # Create users table if it doesn't exist
        conn.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     password TEXT NOT NULL,
                     email TEXT NOT NULL UNIQUE,
                     phone TEXT NOT NULL);''')

        st.write("Enter your credentials to login:")
        name = st.text_input("User name")
        password = st.text_input("Password", type="password")

        col1, col2 = st.columns(2)

        with col1:
                
            aa = st.button("Login")
            
            if aa:


        # if st.button("Login"):
                is_valid, user_name = validate_user(conn, name, password)
                if is_valid:
                    st.success(f"Welcome back, {user_name}! Login successful!")
                    
                    import subprocess
                    subprocess.run(['python','-m''streamlit','run','app.py'])
                    
                    
                    
                else:
                    st.error("Invalid user name or password!")
                    
        with col2:
                  
              aa = st.button("Back")
              
              if aa:
                  import subprocess
                  subprocess.run(['python','-m''streamlit','run','app.py'])
                  # st.success('Successfully Registered !!!')          

        # Close the database connection
        conn.close()
    else:
        st.error("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
