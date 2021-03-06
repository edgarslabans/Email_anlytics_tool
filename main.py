# prblemen "Aero light", "Aero light RE" - opgelostL we kiezen het langste
# Email groeps met hetzelfde subject achter elkaar

objs = list()
email_gr = list()


products = ["Reno Fast", "renofast", "Renosporen", "Reno Dek", "Renodek", "Kolibrie", "Aero", "Aero PD", "Aero Light",
            "Aero light RE", "Aero Riet", "Aero de Luxe", "Aero Verjonging", "Reno Aero PD", "Aero Comfort"]

dakbedekking = ["metaaldak", "velsdak","ongeventileerde","houten dakbedekking"] # update nodig hier


bouwfysica = ["Rc ", "Rc-", ". rc waarde", "damp", "damprem", "densiteit", "warmte", "brand", "brandklasse", "rook",
              "geluid",
              "akoestisch"]
bouwmechanica = ["overspanning", "constructeur", "gording", "afwerking", "dakraamkozijn", "ondersteuning",
                 "Dakhelling (in graden)",
                 "Muurplaat", "tussengording", "nokgording", "lengte", "dakbeschot"]
montage = ["verwerkingsvoorschrift", "verwerking", "monteren", "hijs", "bevestig", "bevestiging","montage"]
certificatie = ["KOMO", "certificaat", "attest"]
nestkast = ["nestkast"]
pasdak = ["pasdak", "Quick Scan"]

montage = []
detailiering = []
overspanningsberekening =[]
andere_constructiev = []
overstek = []
brand = []
TEK_SIPS = []

detailering  =[]


topics_all = [bouwfysica, bouwmechanica, montage, certificatie, nestkast, pasdak]
topics_all_txt = ["bouwfysica", "bouwmechanica", "montage", "certificatie", "nestkast", "pasdak"]


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
            objs.append(Person("", "", "", "", "", "", "", "", "", "", ""))
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

            if "Attachments:" not in Lines[i]:
                if "Categories:" not in Lines[i]:
                    inp = inp + " " + Lines[i].strip()

            rem_ch = ["FW:", "RE:", "Re:", "Fwd:", "NT:"]

            for rem in rem_ch:
                inp = inp.replace(rem, "")

            objs[-1].subject = inp.strip()

        elif "Attachments:" in line.strip():
            objs[-1].bijlage = line.strip().split(" ", 1)[1]

        elif "Categories:" in line.strip():
            objs[-1].categories = line.strip().split(" ", 1)[1]
        elif no_obj_created == False:
            objs[-1].body = objs[-1].subject + " " + objs[-1].bijlage + " " + objs[-1].body + line.strip()


class Person:
    def __init__(email_obj, van, aan, cc, date, subject, bijlage, categories, body, topic,general_topic, product):
        email_obj.van = van
        email_obj.date = date
        email_obj.aan = aan
        email_obj.cc = cc
        email_obj.subject = subject
        email_obj.bijlage = bijlage
        email_obj.categories = categories
        email_obj.body = body
        email_obj.topic = topic
        email_obj.general_topic = general_topic
        email_obj.product = product

    def myfunc(abc):
        # print(abc.subject,abc.van )

        #process "From"
        van_1st_clean = abc.van.split(";", 1)[0]
        van_1st_clean = van_1st_clean.split("<", 1)[0]
        van_1st_clean = van_1st_clean.split("[", 1)[0]

        # process date
        date_clean = abc.date.split(":", 1)[0][:-2]
        rem_ch = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag","zaterdag","zondag"]
        for rem in rem_ch:
            date_clean = date_clean.replace(rem, "").strip()


        print("{:<20}".format(van_1st_clean[:20]), " | ", "{:<15}".format(date_clean[:15]), " | ",
              "{:<50}".format(abc.subject[:50]), " | ","{:<15}".format(abc.product[:15]), " | ",
              "{:<10}".format(abc.categories[:10]), " | ", "{:<15}".format(abc.general_topic[:15])  , " | ",  abc.topic)

        # print(abc.body)


def iter_obj():
    temp = objs[0]

    # merge emails in the groups
    for i in range(1, len(objs)):
        if objs[i - 1].subject[-15:] == objs[i].subject[-15:] or objs[i - 1].subject[:15] == objs[i].subject[:15]:
            objs[i].subject = max(objs[i - 1].subject, objs[i].subject, key=len)
            objs[i].van = objs[i-1].van +";" + objs[i].van
            objs[i].body = objs[i-1].body + objs[i].body
            objs[i].date =  objs[i - 1].date +";" + objs[i].date
            objs[i].categories = objs[i - 1].categories  + objs[i].categories
        else:
            email_gr.append(objs[i - 1])

    # iterating each element in the email_group
    for i in range(len(email_gr)):
        # looking for a product label in the body of email
        tmp_length = 0
        for prod in products:
            if email_gr[i].body.lower().find(prod.lower()) != -1:
                if len(prod) > tmp_length:
                    email_gr[i].product = prod
                    tmp_length = len(prod)

        #looking for a topic
        email_gr[i].topic = {}
        for index, item in enumerate(topics_all, start=0):  # default is zero
            for prop in item:
                # adding topic name to the dictionary if a keyword found
                if email_gr[i].body.lower().find(prop.lower()) != -1:
                    if topics_all_txt[index] not in email_gr[i].topic:
                        email_gr[i].topic.update({topics_all_txt[index]: 1})
                    else:
                        email_gr[i].topic[topics_all_txt[index]] += 1

        # postprocessing topics to find a general topic
        max_key = max(email_gr[i].topic, key=email_gr[i].topic.get)
        if "nestkast" in email_gr[i].topic:
            email_gr[i].general_topic = "nestkast"
        elif "pasdak" in email_gr[i].topic:
            email_gr[i].general_topic = "pasdak"
        else:
            email_gr[i].general_topic = max_key

        email_gr[i].myfunc()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process_pdf()
    print("{:<20}".format("Van"[:20]), " | ", "{:<15}".format("Date"[:15]), " | ",
          "{:<50}".format("Onderwerp"[:50]), " | ", "{:<15}".format("Product"[:15]), " | ",
          "{:<10}".format("Color code"[:10]), " | ", "{:<15}".format("Main cat"[:15]), " | ", "Category")
    print ("----------------------------------------------------------------------------------------------------------"
           "----------------------------------------------------------------------------------------------------------")
    iter_obj()
    print ("Len", len(email_gr))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
