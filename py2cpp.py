"""
A simply python utility for convert Python class source to c++ class source code. I often prototype classes and algorithms in Python,
and have always needed a utility like this. This script requires that a Python class be defined according to certain simplfying constraints, below.
This script is not intended to output a fully defined and compile-able c++ class; in reality, you should always rewrite when doing any sort of language
conversion. The primary intent of this script is to leverage as much of the Python as possible to output c++ source which can then 
be manually reviewed and edited, which still saves tons of c++ overhead writing "myClass::" ten hundred times in your new c++ source.

The python class must be a straightforward Python class. I doubt this script will ever become a full-blown language
converter, and frankly the simpler and less bloated the better. "Simple" meaning keep your Python object as straghtforward and as
cohesive as possible, and this should output c++ class source that can be reviewed, minimally edited, and compiled.

Input example:
	python py2cpp.py [input .py class source file]
Output:
	The script will automatically create and output a class api .h file and a .cpp source file. The names of the files will be the same as the Py class,
	suffixed with "_PROTO".
	Example:
		python py2cpp.py Foo.py
		output:
			Foo_PROTO.h Foo_PROTO.cpp

These translation rules provide the constraints that keep this script robust and useful:
	-Py class must have an __init__ method; this will become the c++ constructor
	-C++ destructor will be unknown. An empty destructor will be produced, and must be manually edited in the output source code.
	-All object functions prepended with "_" will become private members in the c++ class
	-All functions not prepended with "_" and beginning with a capital letter will become the public members of the c++ object api
	-All other functions (ones starting with lower case) will be thrown into the private member section of the c++ class
	-for-loops in Python will be converted as follows, assuming the container will have a size() method:
		Python:							C++:
			for obj in container:			for(int i = 0; i < container.size(); i++){
				obj.do()							container[i].do();
	-All "self." objects that are not a function call will be thrown into the c++ class ctor with UNDEFINED data types. These will have to be manually filled in.
	-No data type inferences will be made wrt Python objects, be they lists, dicts, etc. Maybe I could do this later, but I don't think its very useful, since
	Python container idioms tend to be different in c++; even though the stl supports all basic python containers
	-All private data objects "self.anything" must be defined in the Python __init__ method, and their (empty) types declared.
		Example:
			def __init__:
				self.symbols = ""
				self.listOfStuff = []
				self.tableOfSorts = {}
		This requirement may be useful later, if I decide to parse out the data types of such objects and map them to stl containers/api.
"""



















