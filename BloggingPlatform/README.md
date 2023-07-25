Creating a full-fledged blogging platform is a complex task that goes beyond the scope of a simple Python program. This is a a simplified version of a blogging platform that includes basic features like user authentication, post creation, categorization, and commenting. Keep in mind that a real-world blogging platform would require more robust implementation and security measures.

It needs more functionality, security measures, and styling to make it a complete and secure blogging platform. Additionally, you might want to replace the SQLite database with a more robust database system like PostgreSQL or MySQL for production use.

Explanation:
We set up a Flask app and define a secret key for session management.
The get_db function handles the database connection and is used to execute SQL queries.
The create_tables function initializes the database by executing the SQL schema in "schema.sql". The schema.sql file should be in the same directory as the Python script.
We define routes for the main index ("/"), login ("/login"), post creation ("/create"), and viewing individual posts ("/post/int:post_id").
The index route displays all blog posts in descending order of their IDs.
The login route provides a simple username and password check. For a real-world application, you should use proper authentication mechanisms and databases to store user information securely.
The create route allows users to create new blog posts by submitting a form with title, content, and category.
The post route displays an individual blog post along with its comments. Users can add comments using a form.