

class GUI_Manager:
  """Loads and manages all gui elements.
  Gui elements are seperated by subfolders within a main folder, and can be
  turned on and off at any point.
  Gui elements are stored in xml format.
  Each element has the following properties: req = required, opt = optional
    - Color (req, but it will be ignored if an image is used)
    - Image (opt)
    - Alt image (opt, ignored if there is no image)
    - Text (opt, this is the font, fontsize, text, x offset, and y offset)
    - Width (req, editor will default to the image width if image is used)
    - Height (req, editor will default to the image height if image is used)
    - X position (req)
    - Y position (req)
    - Action (opt, this is the action if it is clicked on)
  """
  def __init__(self, gui_path):
    #gui_path- the main gui path in which other gui subdirectories are contained
    self.gui_path = gui_path