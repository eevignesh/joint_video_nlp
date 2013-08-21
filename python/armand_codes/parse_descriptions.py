#import xml.etree.ElementTree as etree
from lxml import etree
from collections import OrderedDict
from optparse import OptionParser
import os

class MyTriplets:
	V = None
	S = None
	O = None
	idx = None
	def __init__(self, v):
		self.V = v;




#tree = etree.parse('../../../data/CVPR14Vignesh/descriptions/castle_1x02_results_wnt.txt.xml')
def createActionXML(filename):
	tree = etree.parse(filename)
	root = tree.getroot()
	stcs = root.find("document/sentences")
	
	if not stcs:  # careful!
		raise Exception("sentences not found, or sentences is empty")
	if stcs is None:
		raise Exception("sentences not found")
	
	triplets = OrderedDict()
	
	for stc in stcs.iter("sentence"):
		count_verbs = 0
		subtriplets = OrderedDict();
		for tkn in stc.iter("token"):
			if tkn.find("POS").text == "VBZ":
				count_verbs += 1
				subtriplets[tkn.get("id")] = MyTriplets(tkn.find("word").text);
		if count_verbs == 0:
			continue
		print "sentence id=" + stc.get("id")
		
		for deps in stc.iter("dependencies"):
			if "collapsed-ccprocessed-dependencies" == deps.get("type"):
				for dep in deps.iter("dep"):

					# modifier with effect on the verb:
					key = dep.find("governor").get("idx")	
					if key in subtriplets:
						if dep.get("type") == "nsubj":
							subtriplets[key].S = dep.find("dependent").text	
						elif dep.get("type") == "agent":
							subtriplets[key].S =  dep.find("dependent").text	
						elif dep.get("type") == "nsubpass":
							subtriplets[key].O = dep.find("dependent").text if (subtriplets[key].O is None) else subtriplets[key].O + " "+  dep.find("dependent").text	
						elif dep.get("type") == "dobj":
							subtriplets[key].O = dep.find("dependent").text if (subtriplets[key].O is None) else subtriplets[key].O + " "+  dep.find("dependent").text	
						elif dep.get("type") == "rcmod":
							subtriplets[key].O = dep.find("dependent").text if (subtriplets[key].O is None) else subtriplets[key].O + " "+  dep.find("dependent").text	
						elif dep.get("type") == "rel":
							subtriplets[key].O = dep.find("dependent").text if (subtriplets[key].O is None) else subtriplets[key].O + " "+  dep.find("dependent").text	
						elif dep.get("type")[:5] == "prep_":
							subtriplets[key].O = dep.find("dependent").text if (subtriplets[key].O is None) else subtriplets[key].O + " "+  dep.find("dependent").text	
						elif dep.get("type") == "neg":
							subtriplets[key].V +=" "+ dep.find("dependent").text	
						elif dep.get("type") == "prt":
							subtriplets[key].V +=" "+ dep.find("dependent").text	
						elif dep.get("type") == "prep":
							subtriplets[key].V +=" "+ dep.find("dependent").text	
							
		for id, t in subtriplets.iteritems():
			print id, t.S, t.V, t.O
	
		triplets[stc.get("id")] = subtriplets
	
	root = etree.Element("root")
	for stcid, subtriplets in triplets.iteritems():
		for verbid, tr in subtriplets.iteritems():
			node = etree.SubElement(root, "action", {"verbid" : verbid, "stcid" : stcid})
			subject = etree.SubElement(node, "subject")
			subject.text = tr.S	
			verb = etree.SubElement(node, "verb")
			verb.text = tr.V	
			obj = etree.SubElement(node, "object")
			obj.text = tr.O	
	
	tree = etree.ElementTree(root)
	outputname =  os.path.splitext(filename)[0]	
	tree.write(outputname + "_action.xml", pretty_print=True)

parser = OptionParser()
options, arguments = parser.parse_args()

for arg in arguments:
	print arg
	for f in open(arg):
		xmlfile = f.strip() 
 		print xmlfile
    		createActionXML(xmlfile)
		# 'castle_1x02_results_wnt.txt.xml'


