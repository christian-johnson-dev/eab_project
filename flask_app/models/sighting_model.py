from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE



class Sighting:
    def __init__(self, data):
        self.id = data['id']
        self.address = data['address']
        self.city = data['city']
        self.state = data['state']
        self.zip = data['zip']
        self.verification = data['verification']
        self.filename = data['filename']
        self.description = data['description']
        self.date = data['date']
        self.date_created = data['date_created']
        self.date_updated = data['date_updated']





#================== CREATE =================
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO sightings (address, city, state, zip, description, date, filename)
                VALUES (%(address)s, %(city)s, %(state)s, %(zip)s, %(description)s, %(date)s, %(filename)s);
                """
        return connectToMySQL(DATABASE).query_db(query, data)



# #================= GET ALL =================
#     @classmethod
#     def get_all(cls):
#         query = "SELECT * FROM sightings;"
#         results = connectToMySQL(DATABASE).query_db(query)
#         all_sightings = []
#         for row in results:
#             all_sightings.append(cls(row))
#         return all_sightings
        
    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM sightings;
                """
        results = connectToMySQL(DATABASE).query_db(query)
        print('RESULTS =============> \n\n', results)
        all_sightings = []
        if results:
            for row in results:
                # ? Create a sighting
                this_sighting = cls(row)


                # # ? Create the user for this sighting
                # #prepare the dictionary (i.e. entire joined row) for User Constructor
                # user_data = {
                #     **row,  #expands all the keys
                #     'id'            :   row['users.id'],
                #     'created_at'    :   row['users.created_at'],
                #     'updated_at'    :   row['users.updated_at']
                # }
                # # make user
                # this_user = user_model.User(user_data)
                # # add a new attribute
                # this_sighting.creator = this_user
                all_sightings.append(this_sighting)
        return all_sightings



#================== UPDATE =================
    @classmethod
    def update(cls, data):
        query = """
                UPDATE sightings
                SET address = %(address)s, city = %(city)s, state = %(state)s, zip = %(zip)s, verification = %(verification)s, filename = %(filename)s, date = %(date)s
                WHERE id=%(id)s;
                """
        return connectToMySQL(DATABASE).query_db(query, data)



#================== DELETE =================
    @classmethod
    def delete(cls, data):
        query = """
                DELETE FROM sightings
                WHERE id=%(id)s;
                """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results


    @staticmethod
    def validator(form_data):
        print("\n\n<=============IS THIS VALIDATING?=========>\n\n")
        is_valid = True

        #min values
        text_len = 1
            
        if len(form_data['address']) < text_len:
            flash("Missing address")
            is_valid = False

        if len(form_data['city']) < text_len:
            flash("Missing city")
            is_valid = False

        if len(form_data['state']) < text_len:
            flash("Missing state")
            is_valid = False

        if  len(form_data['description']) < 1:
            flash("Missing description")
            is_valid = False

        if  len(form_data['date']) < 1:
            flash("Missing date")
            is_valid = False

        return is_valid