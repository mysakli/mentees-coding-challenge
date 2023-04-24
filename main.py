import pandas as pd
import json



class MenteeSummary:

  def __init__(self, file):
    self.__file = file

    # Load file into a DataFrame
    self.__mentees = pd.read_csv(self.__file)

    # Get number of mentees
    self.__count = self.__mentees.shape[0]

  

    # Calculate average full name length
    self.__mentees[
      'full_name'] = self.__mentees.first_name + ' ' + self.__mentees.last_name
    self.__mentees['name_length'] = self.__mentees.full_name.apply(len)
    self.__avg_name_length = self.__mentees.name_length.mean()

    # Sort by name length and assign ids
    self.sorted_mentees = self.__mentees.sort_values('name_length')
    self.sorted_mentees['length_sorted_id'] = range(1, self.__count + 1)
    self.sorted_mentees.set_index('length_sorted_id', inplace=True)
  
  def get_count(self):
    return self.__count

  def get_avg_name_length(self):
        return self.__avg_name_length
  
  # Find the shortest full name(s)
  def get_shortest_name(self):
    i = 1
    shortest_name = {self.sorted_mentees.loc[i]['full_name']}
    while self.sorted_mentees.loc[i]['name_length'] == self.sorted_mentees.loc[
        i + 1]['name_length']:
      shortest_name.update((self.sorted_mentees.loc[i]['full_name'],
                            self.sorted_mentees.loc[i + 1]['full_name']))
      i += 1
      if i > self.__count:
        break
    return sorted(list(shortest_name))

  # Find the longest full name(s)
  def get_longest_name(self):
    longest_name = {self.sorted_mentees.loc[self.__count]['full_name']}
    i = self.__count
    while self.sorted_mentees.loc[i]['name_length'] == self.sorted_mentees.loc[
        i - 1]['name_length']:
      longest_name.update((self.sorted_mentees.loc[i]['full_name'],
                           self.sorted_mentees.loc[i - 1]['full_name']))
      i -= 1
      if i < 1:
        break

    return sorted(list(longest_name))

  # Get unique languages
  def get_unique_languages(self):
    languages = self.__mentees.language
    unique_languages = set()
    for l in languages:
      unique_languages.add(l)
    return sorted(list(unique_languages))

  # Create a summary JSON file
  def create_summary_json(self, file_name):
    summary = {
      'nr_of_mentees': self.__count,
      'languages': self.get_unique_languages(),
      'avg_name_length': self.__avg_name_length,
      'shortest_names': self.get_shortest_name(),
      'longest_names': self.get_longest_name()
    }
    with open(file_name, 'w') as outfile:
      json.dump(summary, outfile, indent=4)


mentee_summary = MenteeSummary('mentee-list.csv')
mentee_summary.create_summary_json('mentees-summary.json')


