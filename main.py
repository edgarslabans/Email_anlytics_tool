# prblemen "Aero light", "Aero light RE"

objs = list()
email_gr = list()

products = ["Reno fast", "renofast","Renosporen", "Reno dek", "Renodek","Kolibrie", "Aero","Aero PD", "Aero Light", "Aero light RE","Unidek Aero Riet", "Aero de Luxe","Aero verjonging","Reno Aero PD","Aero Comfort"]

bouwfysica = ["Rc ","Rc-","damp","damprem", "densiteit", "warmte","brand","brandklasse","rook","geluid","akoestisch"]
bouwmechanica = ["overspanning", "gording", "afwerking","dakraamkozijn","ondersteuning","Dakhelling (in graden)","Muurplaat", "tussengording", "nokgording","lengte","dakbeschot"]
montage = ["verwerkingsvoorschrift", "monteren", "hijs","bevestig"]
certificatie = ["KOMO", "certificaat","attest"]
nestkast = ["nestkast"]
pasdak = ["pasdak"]


def process_pdf():
    # Python code to
    # demonstrate readlines()

    L = []

    # Using readlines()
    file1 = open('month1.txt', 'r', encoding="utf-8")
    Lines = file1.readlines()

    count = 0
    no_obj_created = True

    # Strips the newline character
    for i in range(len(Lines)):
        line = Lines[i]
        i += 1

        if "From:" in line.strip() or "Van:" in line.strip():
            objs.append(Person("", "", "", "", "", "", "" ,"", "" ,""))
            no_obj_created = False

            objs[-1].van = line.strip().split(" ", 1)[1]

        elif "Sent:" in line.strip() or "Verzonden:" in line.strip():
            objs[-1].date = line.strip().split(" ", 1)[1]

        elif "To:" in line.strip() or "Aan:" in line.strip():
            objs[-1].aan = line.strip().split(" ", 1)[1]
        elif "CC:" in line.strip() or "Cc:" in line.strip():
            objs[-1].cc = line.strip().split(" ", 1)[1]

        elif "Subject:" in line.strip() or "Onderwerp:" in line.strip():
            inp = line.strip().split(" ", 1)[1]

            rem_ch = ["FW:", "RE:" ,"Re:" ,"Fwd:", "NT:"]

            for rem in rem_ch:
                inp = inp.replace(rem, "")


            objs[-1].subject = inp.strip()

        elif "Attachments:" in line.strip():
            objs[-1].bijlage = line.strip().split(" ", 1)[1]

        elif "Categories:" in line.strip():
            objs[-1].categories = line.strip().split(" ", 1)[1]
        elif no_obj_created == False:
            objs[-1].body = objs[-1].body + line.strip()


class Person:
    def __init__(email_obj, van, aan, cc ,date, subject, bijlage, categories, body,topic, product):
        email_obj.van = van
        email_obj.date = date
        email_obj.aan = aan
        email_obj.cc = cc
        email_obj.subject = subject
        email_obj.bijlage = bijlage
        email_obj.categories = categories
        email_obj.body = body
        email_obj.topic = topic
        email_obj.product = product

    def myfunc(abc):
        # print(abc.subject,abc.van )
        print(abc.subject," === ", abc.product)


def iter_obj():
    temp = objs[0]

    #merge emails in the groups
    for i in range(1,len(objs)):
        if objs[i-1].subject[-5:] == objs[i].subject[-5:] or objs[i-1].subject[:5] == objs[i].subject[:5]:
            objs[i].subject = max(objs[i-1].subject, objs[i].subject , key = len)
            objs[i].van = objs[i].van + objs[i-1].van
            objs[i].body = objs[i].body + objs[i - 1].body
        else:
            email_gr.append(objs[i-1])

    # sorting
    for i in range(len(email_gr)):
        tmp_length = 0
        for prod in products:
            if email_gr[i].body.lower().find(prod.lower()) != -1:
                if len(prod) > tmp_length:
                    email_gr[i].product = prod
                    tmp_length = len(prod)

        email_gr[i].myfunc()




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process_pdf()
    iter_obj()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/