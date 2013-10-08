from XMLModel import XMLModel
from .Instance import Instance
from rightscale.util import ElementTreeValueOK

class Instances(XMLModel):

  def __init__(self, data=None, rsapi=None):
    self.instances = list()
    super(Instances, self).__init__(data, rsapi)

  def __len__(self):
    return len(self.instances)

  def __getitem__(self, index):
    return self.instances[index]

  def __iter__(self):
    return iter(self.instances)

  def add_instance(self, data):
    instance = Instance(data, self.rsapi)
    self.instances.append(instance)

  ELEMENTS = {
    "instance": add_instance,
  }

