import xml.etree.ElementTree as ET

# Import source XML
tree = ET.parse('sfe.xml')
root = tree.getroot()
print(root)

# Print highest level XML-tag
print(root.tag)
print(root.attrib)

# Print all tags and attributes on next level
for child in root:
    print(child.tag,child.attrib)

# Save lpc and networkindicator for SS7
local_pc = child.attrib['lpc']
networkindicator = child.attrib['networkindicator']

# Convert networkindicator to integer
if networkindicator == 'international0':
   network = 0
elif networkindicator == 'international1':
   network = 1
elif networkindicator == 'national0':
   network = 2
elif networkindicator == 'national1':
   network = 3
else:
   network = 0
# This should not happen 

# Print tag for next lexel
print("M3UA",)
for M3UA in root.iter('M3UA'):
    print(M3UA.attrib)

# Save attrbutes for M3UA
aspid = M3UA.attrib['asp_id']
network_app = M3UA.attrib['network_appearance']
ipp = M3UA.attrib['primary_ip']
rc = M3UA.attrib['routing_context']

# Define list for multiple tags
sgs = []
sgip = []
route_sgs = []

# Print next tags and attributes on next level
for SG in root.iter('SG'):
    print("SG",SG.attrib)
    sgs.append(SG.attrib['sg_id'])

# Print next tags and attributes on next level
for SG_LINK in root.iter('SG_LINK'):
    print("SG_LINK",SG_LINK.attrib)
    sgip.append(SG_LINK.attrib['primary_ip'])

# Up one level, print tag and attribute
print("M3UA_ROUTE",)
for M3UA_ROUTE in root.iter('M3UA_ROUTE'):
    print(M3UA_ROUTE.attrib)
dest_pc = M3UA_ROUTE.attrib['dpc']

# Print next tags and attributes on next level
for M3UA_ROUTE_SG in root.iter('M3UA_ROUTE_SG'):
    print("M3UA_ROUTE_SG",M3UA_ROUTE_SG.attrib)
    route_sgs.append(M3UA_ROUTE_SG.attrib['sg'])


# Up one level, print tag and attribute
print("SCCP",)
for SCCP in root.iter('SCCP'):
    print(SCCP.attrib)

route_cgpa_gt = SCCP.attrib['route_cgpa_on_gt']
xudt = SCCP.attrib['xudt']

# Print next tags and attributes on next level
for RSP in root.iter('RSP'):
    print("RSP",RSP.attrib)

rss_dest_pc = RSP.attrib['pc']

# Print next tags and attributes on next level
for RSS in root.iter('RSS'):
    print("RSS",RSS.attrib)

rss_ssn = RSS.attrib['ssn']

# Up one level, print tag and attribute
for LSS in root.iter('LSS'):
    print("LSS",LSS.attrib)

lss_ssn = LSS.attrib['ssn']

# Print next tags and attributes on next level
for CONCERNED in root.iter('CONCERNED'):
    print("CONCERNED",CONCERNED.attrib)

concerned_pc = CONCERNED.attrib['pc']

print("LOAD OUTPUT XML")
 
# Load outpt XML
tree = ET.parse('cfe.xml')
root = tree.getroot()
print(root)

# Print highest level XML-tag
print(root.tag)
print(root.attrib)

# Print all tags and attributes on next level
for child in root.iter('HOST'):
    print(child.tag,child.attrib)

child.attrib['IP'] = ipp

for child in root:
    print(child.tag,child.attrib)
    
# Print all tags for next lexel
print("M3UA",)
for M3UA in root.iter('M3UA'):
    print(M3UA.attrib)

for SG in root.iter('SG'):
    print("SG",SG.attrib)

for ROUTE_SG in root.iter('ROUTE_SG'):
    print("ROUTE_SG",ROUTE_SG.attrib)

for SCCP in root.iter('SCCP'):
    print("SCCP",SCCP.attrib)

for RSS in root.iter('RSS'):
    print("RSS",RSS.attrib)

for LSS in root.iter('LSS'):
    print("LSS",LSS.attrib)

# Modify
child.attrib['Local_PC'] = local_pc 
child.attrib['Network'] = str(network)


# Modify M3UA attributes
M3UA.attrib['ASPID'] = aspid
M3UA.attrib['Network_app'] = network_app
M3UA.attrib['IPP'] = ipp
M3UA.attrib['RC'] = rc

# Modify SG attributes
i=0
for SG in root.iter('SG'):
    SG.attrib['ID'] = sgs[i]
    SG.attrib['IP'] = sgip[i]
    i += 1

# Modify ROUTE_SG attributes
i=0
for ROUTE_SG in root.iter('ROUTE_SG'):
    ROUTE_SG.attrib['sg'] = route_sgs[i]
    ROUTE_SG.attrib['Destination_PC'] = dest_pc
    i += 1

# Modify SCCP attrbutes
SCCP.attrib['route_cgpa_on_gt'] = route_cgpa_gt
SCCP.attrib['xudt'] = xudt

# Modify RSS attributes
RSS.attrib['Destination_PC'] = rss_dest_pc
RSS.attrib['ssn'] = rss_ssn

# Modify SSN attributes
LSS.attrib['Concerned_PC'] = concerned_pc
LSS.attrib['ssn'] = lss_ssn
 
tree.write('cfe.xml')



