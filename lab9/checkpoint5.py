from pymongo import MongoClient
import random
import datetime
client = MongoClient()
db = client.csci2963
collection = db.definitions

def random_word_requester():
	random.seed()
	count = 0
	index = random.randint(0,collection.count()-1)
	for x in collection.find():
		if (count == index):
			collection.update_one(x,{'$push': {'dates': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}})
			return collection.find_one(x)
		count = count + 1
	return


if __name__ == '__main__':
    print random_word_requester()
