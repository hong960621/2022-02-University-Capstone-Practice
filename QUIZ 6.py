#Quiz 6) Code a program that read and write data to a pickle file.

import pickle                                                                   # Enable module 'Pickle'

profile = {'ID': 'cms', 'age': 20, 'hobby': ['coding', 'chemistry', 'physics']} # Declare profile and save all perosnal information in dictionary form

with open('profile.pickle','wb') as fw:                                         # Save 'profile' as pickle file
    pickle.dump(profile, fw)

with open('profile.pickle', 'rb') as fr:                                        # Load 'profile' 
    profile_loaded = pickle.load(fr)                                            # Save pickle file 'profile' as a variable

print(profile_loaded)                                                           # Print out personal information, which is saved in the variable