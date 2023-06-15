import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

DB_SETTINGS = {
    'db': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'passwd': os.getenv('DB_PASS'),
    'host': os.getenv('DB_HOST'),
}

# Установить общее соединение
cnx = None

def get_connection():
    global cnx
    if cnx is None:
        cnx = mysql.connector.connect(**DB_SETTINGS)
    return cnx

def get_domains():
    try:
        cnx = get_connection()
        cursor = cnx.cursor()
        query = "SELECT domain FROM domains;"
        cursor.execute(query)
        domains = [item[0] for item in cursor.fetchall()]
        return domains
    except mysql.connector.Error as err:
        print(f"Error while retrieving domains: {err}")
        return []

def get_page_id(domain):
    try:
        cnx = get_connection()
        cursor = cnx.cursor()
        query = f'SELECT id FROM domains WHERE domain = "{domain}";'
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            return result[0]
        return None
    except mysql.connector.Error as err:
        print(f"Error while retrieving page ID: {err}")
        return None

def insert_link(from_page_id, to_page_id):
    try:
        cnx = get_connection()
        cursor = cnx.cursor()
        query = f"INSERT INTO links (from_page_id, to_page_id) VALUES ({from_page_id}, {to_page_id});"
        cursor.execute(query)
        cnx.commit()
    except mysql.connector.Error as err:
        print(f"Error while inserting link: {err}")
