##Lab 9

###Louis Silvestro

1. MongoDB daemon:

   ![mongod.png](images/mongod.png)

   MongoDB client:
   
   ![mongo.png](images/mongo.png)

2. Import data:

   ![import.png](images/import.png)

3. Basic queries:

   Use database and definitions:

   ![setup.png](images/setup.png)

   find(): list all documents in the database:

   ![find.png](images/find.png)

   findOne(): list the first document in the database

   ![findOne.png](images/findOne.png)

   find({word: "Capitaland"}): display the document with "Capitaland" as the value of the word field

   ![capitaland.png](images/capitaland.png)

   find({_id: ObjectId("56fe9e22bad6b23cde07b8ce")}): find document with specified object id

   ![object.png](images/object.png)

   A definition for git was inserted into the database and updated:

   ![update.png](images/update.png)

   export database to json file:

   ![export.png](images/export.png)

4. Driving Queries

   code of python file: [checkpoint4.py]

5. Random Word Requester

   code: [checkpoint5.py]
