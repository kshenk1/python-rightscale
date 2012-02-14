from XMLModel import XMLModel
from .Array import Array
from rightscale.util import ElementTreeValueOK

class Arrays(XMLModel):

  def __init__(self, data=None, rsapi=None):
    self.arrays = list()
    super(Arrays, self).__init__(data, rsapi)

  def __len__(self):
    return len(self.arrays)

  def __getitem__(self, index):
    return self.arrays[index]

  def __iter__(self):
    return iter(self.arrays)

  def add_array(self, data):
    array = Array(data, self.rsapi)
    self.arrays.append(array)

  ELEMENTS = {
    "server-array": add_array,
  }

