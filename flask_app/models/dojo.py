from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninja import Ninja


# model the class after the dojos table from our database
class Dojo:
    def __init__( self, data ):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    # READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninjas").query_db(query)
        
        print("This is data inside of results from running get all query", results)
        
        dojos = []
        
        # Iterate over the db results and create instances of dojos with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        
        return dojos

    # CREATE
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)
        
        print("This is the data inside of the results after we insert into database", results)

        return results


    #READ ONE
    @classmethod
    def get_one_dojo(cls, data):
        query="SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas").query_db(query, data)

        if len(results) == 0:
            return False

        dojo = Dojo(results[0])

        if results[0]["ninjas.id"] != None:
            for row in results:
                ninjaData = {
                    "id": row["ninjas.id"],
                    "dojo_id": row["dojo_id"],
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "age": row["age"],
                    "created_at": row["ninjas.created_at"],
                    "updated_at": row["ninjas.updated_at"]
                }
                print(ninjaData)
                dojo.ninjas.append(Ninja(ninjaData))

        return dojo





