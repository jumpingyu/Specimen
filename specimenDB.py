# Do not edit this file or it may not load correctly
# if you try to open it with the RSG Dialog Builder.

# Note: thisDir is defined by the Activator class when
#       this file gets exec'd

from rsg.rsgGui import *
from abaqusConstants import INTEGER, FLOAT
dialogBox = RsgDialog(title='Create Specimen', kernelModule='kernel', kernelFunction='create_specimen', includeApplyBtn=True, includeSeparator=True, okBtnText='OK', applyBtnText='Apply', execDir=thisDir)
RsgTabBook(name='TabBook_2', p='DialogBox', layout='0')
RsgTabItem(name='TabItem_2', p='TabBook_2', text='Part')
RsgLabel(p='TabItem_2', text='Note: Create the part of the tubular specimen.', useBoldFont=True)
RsgCheckButton(p='TabItem_2', text='Create parts', keyword='run_part_module', default=True)
RsgHorizontalFrame(name='HFrame_2', p='TabItem_2', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgGroupBox(name='GroupBox_5', p='HFrame_2', text='Parameters', layout='0')
RsgVerticalAligner(name='VAligner_3', p='GroupBox_5', pl=0, pr=0, pt=0, pb=0)
RsgTextField(p='VAligner_3', fieldType='Float', ncols=12, labelText='Gauge Length:', keyword='gauge_length', default='35.0')
RsgTextField(p='VAligner_3', fieldType='Float', ncols=12, labelText='Specimen Length:', keyword='specimen_length', default='180.0')
RsgTextField(p='VAligner_3', fieldType='Float', ncols=12, labelText='Grip Length:', keyword='grip_length', default='60.0')
RsgTextField(p='VAligner_3', fieldType='Float', ncols=12, labelText='Inner Radius:', keyword='inner_radius', default='5.0')
RsgTextField(p='VAligner_3', fieldType='Float', ncols=12, labelText='Outer Radius:', keyword='outer_radius', default='8.0')
RsgTextField(p='VAligner_3', fieldType='Float', ncols=12, labelText='Outer Radius in Gauge Length:', keyword='outer_radius_in_gauge_length', default='6.0')
RsgTextField(p='VAligner_3', fieldType='Float', ncols=12, labelText='R1:', keyword='R1', default='1.0')
RsgTextField(p='VAligner_3', fieldType='Float', ncols=12, labelText='R2:', keyword='R2', default='0.2')
RsgTextField(p='VAligner_3', fieldType='Float', ncols=12, labelText='Theta:', keyword='theta', default='18.0')
RsgGroupBox(name='GroupBox_4', p='HFrame_2', text='Schematic', layout='0')
RsgIcon(p='GroupBox_4', fileName='1.png')
RsgTabItem(name='TabItem_3', p='TabBook_2', text='Mesh')
RsgLabel(p='TabItem_3', text='Note: Create mesh of the tubular specimen.', useBoldFont=True)
RsgCheckButton(p='TabItem_3', text='Create mesh', keyword='run_mesh_module', default=True)
RsgHorizontalFrame(name='HFrame_4', p='TabItem_3', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgGroupBox(name='GroupBox_7', p='HFrame_4', text='Seeds of the mesh', layout='0')
RsgVerticalAligner(name='VAligner_4', p='GroupBox_7', pl=0, pr=128, pt=0, pb=0)
RsgTextField(p='VAligner_4', fieldType='Integer', ncols=12, labelText='Seed 1:', keyword='seed_1', default='30')
RsgTextField(p='VAligner_4', fieldType='Integer', ncols=12, labelText='Seed 2:', keyword='seed_2', default='15')
RsgTextField(p='VAligner_4', fieldType='Integer', ncols=12, labelText='Seed 3:', keyword='seed_3', default='15')
RsgTextField(p='VAligner_4', fieldType='Integer', ncols=12, labelText='Seed 4:', keyword='seed_4', default='15')
RsgTextField(p='VAligner_4', fieldType='Integer', ncols=12, labelText='Seed 5:', keyword='seed_5', default='4')
RsgTextField(p='VAligner_4', fieldType='Integer', ncols=12, labelText='Seed 6:', keyword='seed_6', default='15')
RsgTextField(p='VAligner_4', fieldType='Integer', ncols=12, labelText='Seed 7:', keyword='seed_7', default='15')
RsgTextField(p='VAligner_4', fieldType='Integer', ncols=12, labelText='Seed 8:', keyword='seed_8', default='15')
RsgTextField(p='VAligner_4', fieldType='Integer', ncols=12, labelText='Seed 9:', keyword='seed_9', default='15')
RsgTextField(p='VAligner_4', fieldType='Integer', ncols=12, labelText='Seed 10:', keyword='seed_10', default='15')
RsgTextField(p='VAligner_4', fieldType='Integer', ncols=12, labelText='Seed 11:', keyword='seed_11', default='15')
RsgTextField(p='VAligner_4', fieldType='Integer', ncols=12, labelText='Seed 12:', keyword='seed_12', default='15')
RsgTextField(p='VAligner_4', fieldType='Integer', ncols=12, labelText='Seed 13:', keyword='seed_13', default='15')
RsgTextField(p='VAligner_4', fieldType='Integer', ncols=12, labelText='Seed 14:', keyword='seed_14', default='15')
RsgGroupBox(name='GroupBox_6', p='HFrame_4', text='Schematic', layout='0')
RsgIcon(p='GroupBox_6', fileName='2.png')
RsgTabItem(name='TabItem_4', p='TabBook_2', text='Material')
RsgLabel(p='TabItem_4', text='Note: Create materials and sections.', useBoldFont=True)
RsgCheckButton(p='TabItem_4', text='Define materials', keyword='run_material_module', default=True)
RsgHorizontalFrame(name='HFrame_7', p='TabItem_4', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgGroupBox(name='GroupBox_10', p='HFrame_7', text='Parameters', layout='0')
RsgVerticalAligner(name='VAligner_6', p='GroupBox_10', pl=0, pr=0, pt=0, pb=0)
RsgCheckButton(p='GroupBox_10', text='GH4169', keyword='material_GH4169', default=True)
RsgCheckButton(p='GroupBox_10', text='User defined material', keyword='material_user', default=False)
RsgFileTextField(p='GroupBox_10', ncols=50, labelText='File name:', keyword='umat_filename', default='', patterns='All files (*)')
RsgTabItem(name='TabItem_8', p='TabBook_2', text='Assembly')
RsgLabel(p='TabItem_8', text='Note: Create assembly.', useBoldFont=True)
RsgCheckButton(p='TabItem_8', text='Create assembly', keyword='run_assembly_module', default=True)
RsgTabItem(name='TabItem_5', p='TabBook_2', text='Step')
RsgLabel(p='TabItem_5', text='Note: Create steps.', useBoldFont=True)
RsgCheckButton(p='TabItem_5', text='Create steps', keyword='run_step_module', default=True)
RsgHorizontalFrame(name='HFrame_6', p='TabItem_5', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgGroupBox(name='GroupBox_9', p='HFrame_6', text='Parameters', layout='0')
RsgVerticalAligner(name='VAligner_5', p='GroupBox_9', pl=0, pr=0, pt=0, pb=0)
RsgTextField(p='VAligner_5', fieldType='Float', ncols=12, labelText='Time period:', keyword='timePeriod', default='1')
RsgTextField(p='VAligner_5', fieldType='Integer', ncols=12, labelText='Maximum number of increments:', keyword='maxNumInc', default='10000')
RsgTextField(p='VAligner_5', fieldType='Float', ncols=12, labelText='Initial increment size:', keyword='initialInc', default='0.1')
RsgTextField(p='VAligner_5', fieldType='Float', ncols=12, labelText='Minimum increment size:', keyword='minInc', default='0.00001')
RsgTextField(p='VAligner_5', fieldType='Float', ncols=12, labelText='Maximum increment size:', keyword='maxInc', default='1')
RsgTabItem(name='TabItem_6', p='TabBook_2', text='Load')
RsgLabel(p='TabItem_6', text='Note: Create loads.', useBoldFont=True)
RsgCheckButton(p='TabItem_6', text='Define loads', keyword='run_load_module', default=True)
RsgHorizontalFrame(name='HFrame_5', p='TabItem_6', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgGroupBox(name='GroupBox_8', p='HFrame_5', text='Parameters', layout='0')
RsgVerticalAligner(name='VAligner_12', p='GroupBox_8', pl=0, pr=0, pt=0, pb=0)
RsgTextField(p='VAligner_12', fieldType='Integer', ncols=12, labelText='Loading cycles:', keyword='loading_cycles', default='20')
RsgTextField(p='VAligner_12', fieldType='Float', ncols=12, labelText='Displacement:', keyword='displacement_value', default='1')
RsgTextField(p='VAligner_12', fieldType='Float', ncols=12, labelText='Rotation(rad):', keyword='rotation_value', default='0.1')
RsgTextField(p='VAligner_12', fieldType='Float', ncols=12, labelText='Force:', keyword='force_value', default='1')
RsgTextField(p='VAligner_12', fieldType='Float', ncols=12, labelText='Torque:', keyword='torque_value', default='1')
RsgTextField(p='VAligner_12', fieldType='Float', ncols=12, labelText='Temperature:', keyword='temperature_value', default='1')
RsgHorizontalFrame(name='HFrame_12', p='GroupBox_8', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgCheckButton(p='HFrame_12', text='Displacement', keyword='add_displacement', default=True)
RsgCheckButton(p='HFrame_12', text='Rotation', keyword='add_rotation', default=True)
RsgCheckButton(p='HFrame_12', text='Force', keyword='add_force', default=False)
RsgCheckButton(p='HFrame_12', text='Torque', keyword='add_torque', default=False)
RsgCheckButton(p='HFrame_12', text='Temperature', keyword='add_temperature', default=False)
RsgSeparator(p='GroupBox_8')
RsgLabel(p='GroupBox_8', text='Amplitudes:', useBoldFont=False)
RsgTable(p='GroupBox_8', numRows=5, columnData=[('Time', 'Float', 100), ('Displacement', 'Float', 100), ('Roatation', 'Float', 100), ('Force', 'Float', 100), ('Torque', 'Float', 100), ('Temperature', 'Float', 100)], showRowNumbers=True, showGrids=True, keyword='loading_conditions', popupFlags='AFXTable.POPUP_CUT|AFXTable.POPUP_COPY|AFXTable.POPUP_PASTE|AFXTable.POPUP_INSERT_ROW|AFXTable.POPUP_DELETE_ROW|AFXTable.POPUP_CLEAR_CONTENTS|AFXTable.POPUP_READ_FROM_FILE|AFXTable.POPUP_WRITE_TO_FILE')
RsgTabItem(name='TabItem_7', p='TabBook_2', text='Job')
RsgLabel(p='TabItem_7', text='Note: Create jobs.', useBoldFont=True)
RsgCheckButton(p='TabItem_7', text='Create jobs', keyword='run_job_module', default=True)
RsgHorizontalFrame(name='HFrame_8', p='TabItem_7', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgGroupBox(name='GroupBox_11', p='HFrame_8', text='Parameters', layout='0')
RsgTextField(p='GroupBox_11', fieldType='String', ncols=12, labelText='Job name:', keyword='job_name', default='Job-1')
RsgCheckButton(p='GroupBox_11', text='Write the input file', keyword='write_input', default=True)
RsgCheckButton(p='GroupBox_11', text='Save the cae file as:', keyword='write_cae', default=True)
RsgFileTextField(p='GroupBox_11', ncols=50, labelText='File name:', keyword='cae_filename', default='', patterns='*.cae')
RsgCheckButton(p='GroupBox_11', text='Submit', keyword='submit_job', default=False)
dialogBox.show()