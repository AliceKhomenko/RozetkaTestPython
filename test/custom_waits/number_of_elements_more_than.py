class number_of_element_more_than(object):
  """An expectation for checking that an element has a particular css class.

  locator - used to find the element
  returns the WebElement once it has the particular css class
  """
  def __init__(self, locator, number):
    self.locator = locator
    self.number = number

  def __call__(self, driver):
    elements = driver.find_elements(*self.locator)   # Finding the referenced element
    if len(elements)>self.number:
        return True
    else:
        return False

# Wait until an element with id='myNewInput' has class 'myCSSClass'

