from pyscript import document, when

grade_7 = {'Aeris Bandong', 'Adriana Averilla', 'Carlos David', 'Ciara De Guzman', 'Cianna Del Prado', 'Caitlyn Tano', 'Christopher De Vera'}
grade_8 = {'Jacqueline Tian', 'Mandy Cajanding', 'Myka Dela Rosa', 'Gabriel De Jesus', 'Julia Bermudez', 'Kirsten Imam'}
grade_9 = {'Zyrene Nieto', 'Margareth Chiong', 'Parminder Bhullar', 'Rachel Balasico', 'Raphael Buan'}
grade_10 = {'Wenz Paragas', 'Hanzo Del Rosario', 'Ian Salangsang', 'Jan Cabading', 'Jude Yunus', 'Dustin Cunanan', 'Rafael Roncal'}

def update_ui(master_set):
    sorted_list = sorted(master_set)
    formatted_members = '<br>'.join(sorted_list)
    
    output_html = f"<div class='result-title'>ALL MEMBERS:</div><div>{formatted_members}</div><div class='total-count'>TOTAL MEMBERS: {len(master_set)}</div>"
    
    document.querySelector('#result').innerHTML = output_html

initial_master = grade_7 | grade_8 | grade_9 | grade_10
update_ui(initial_master)

@when('click', '#add-btn')
def add_member(event=None):
    first_name = document.querySelector('#first-name').value.strip()
    last_name = document.querySelector('#last-name').value.strip()
    
    full_name = f'{first_name} {last_name}'.strip().title()
    new_member_set = {full_name}
    
    master_set = grade_7 | grade_8 | grade_9 | grade_10 | new_member_set
    master_set = master_set - {''}
    
    update_ui(master_set)
    
    document.querySelector('#first-name').value = ''
    document.querySelector('#last-name').value = ''