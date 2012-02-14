from setuptools import setup, find_packages

setup(name="rightscale",
      version="0.310",
      description="Object-oriented library for RightScale's API.",
      author="Jordan Sissel",
      author_email="jordan@loggly.com",
      url="none-yet",
      zip_safe=False,
      packages=find_packages(),
      # package_dir = { 
      #   "rightscale": "src/rightscale",
      #   "rightscale.util": "src/rightscale/util",
      # },
      requires=["httplib2", "netifaces"],
      )

