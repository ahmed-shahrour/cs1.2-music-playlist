class Song:

  def __init__(self, title):
      self.__title = title
      self.__next_song = None


  # TODO: Create a getter method for the title attribute, called get_title
  def get_title(self):
    return self.__title
  
  
  # TODO: Create a setter method for the next_song attribute, called set_title. Make sure titles are type cased to strings and are Title Cased.
  def set_title(self, title):
    if not isinstance(title, str):
      return print(f"ERROR: Failed to set title, {title} is not type string")
      
    if not title.istitle():
      return print(f"ERROR: Failed to set title, {title} is not title case")
      
    self.__title = title

  # TODO: Create a getter method for the next_song attribute, called get_next_song
  def get_next_song(self):
    return self.__next_song


  # TODO: Create a setter method for the next_song attribute, called set_next_song
  def set_next_song(self, next_title):
    if not isinstance(next_title, str):
      return print(f"ERROR: Failed to set title, {next_title} is not type string")
      
    if not next_title.istitle():
      return print(f"ERROR: Failed to set title, {next_title} is not title case")
    
    self.__next_song = next_title


  # TODO: Using the __str___ dunder method, return a string of the song title.
  def __str__(self):
    return self.get_title()


  # TODO: Using the __repr__ dunder method, return a string formatted as the following:'Song Title -> Next Song Title'
  def __repr__(self):
    pass
