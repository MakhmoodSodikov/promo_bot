INS = """INSERT INTO Dialogs VALUES('{}', '{}', '{}', '{}');"""

CREATE = """
CREATE TABLE IF NOT EXISTS Dialogs (
                               Dialog_ID INTEGER, 
                               Name_NM TEXT, 
                               Username_NM text, 
                               Progress integer);"""

FIND_USER = '''
SELECT Dialog_ID 
  FROM Dialogs 
 WHERE Dialog_ID = {};
'''

GET_PROGRESS = '''
SELECT Progress 
  FROM Dialogs 
 WHERE Dialog_ID = {};
'''

UPD_PROGRESS = '''
UPDATE Dialogs
  SET Progress = {} 
WHERE Dialog_ID = {}
'''

GET_USERS_PROGMIN = """
   SELECT Dialog_ID 
     FROM Dialogs 
WHERE not Progress = -1 
"""
