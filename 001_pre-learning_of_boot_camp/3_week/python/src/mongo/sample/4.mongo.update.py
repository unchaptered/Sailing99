db.users.update_one({ 'name': 'bobby' }, { '$set': { 'age': 19 } })