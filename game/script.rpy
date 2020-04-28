# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define AH = Character("Anne Hinson")
define B = Character("Mrs. Blundin")
define TM = Character("Thomas McElwee")
define SW = Character("Warden Samuel R. Wood")
define CD = Character("Charles R. Demmy")
define leg1 = Character("Henry Bingham")
define leg2 = Character("Horace Binney")
define leg3 = Character("Harold Bingley")
define BC = Character("Benjamin Coates")
define WB = Character("William Baen")
define Y = Character("You")
define R = Character("Mr.Richards")
define O = Character("Officer")
define E = Character("Examiner")
define TL = Character("Thomas Larcombe")

# Declare the images

# Backgrounds
image sepia = "#f2cc85"
image black = "#000"
image esp = "esp.jpg"
image esp_whole = "esp_whole.jpg"
image esp_front = "esp_front_gate_vt.jpg"
image gatekeeper_room = "esp_gatekeeper.jpg"
image cell_intake = "esp_cell_intake.jpg"
image cell = "esp_cell.jpg"
image basement = "esp_basement.jpg"
image stairs = "esp_stairs.jpg"
image hallway = "esp_hallway.jpg"
image mc_wood = "esp_mc_wood.jpg"
image rotunda = "esp_rotunda.jpg"
image yard = "esp_yard.jpg"
image scene6gate = "esp_inside_gate.jpg"
image hearingroom = "hearingroom.png"

# Characters
image officer = "officer.png"
image examiner = "examiner.png"
image blundin = "blundin.png"
image court_blundin = "blundin2.png"
image warden = "warden.png"
image hinson = "hinson.png"
image mcelwee = "mcelwee.png"
image mcelwee_right = "mcelwee_right.png"
image demmy = "demmy.png"
image baen = "baen.png"
image richards = "richards.png"
image larcombe = "larcombe.png"
image leg1 = "leg1.png"
image leg2 = "leg2.png"
image leg3 = "leg3.png"

# The game starts here.

label start:

    menu:
        "Play as a new female inmate":
            jump hinson_storyline
        "Play as Thomas McElwee's assistant, inspecting the prison":
            jump mc_intro


# Hinson Scene 1-2

label hinson_storyline:

    "It’s November 1833. A few days ago, you poisoned your abusive husband in self-defense after he drunkenly beat you up for the sixth time that week alone. You figured if you didn’t do something soon, he was going to kill you."

    "He survived, and had you taken to the penitentiary, hoping that the solitary confinement will teach you lessons in moral conduct and penitence — really, he just wanted to get rid of you."

    scene esp_whole
    with dissolve

    "You stand a few feet outside Eastern State penitentiary, escorted by an officer."

    "The officer fumbles about, not sure where to grab you. He winks sleazily at you."

    show officer

    O "You’re my first woman I’ve had to handle as an inmate. Come on, we’re almost there."

    with dissolve
    scene esp_front

    "Once through the peripheral gateway, you are led quickly to the buildings on the west side of the compound. You steal your first glimpse at the outside of the main tour, and the cellblocks radiating off it. "

    scene gatekeeper_room

    "You are led inside, to the gatekeeper’s room. There’s a woman and three men standing inside, laughing and joking. One of the men wearing a doctor’s coat steps forward. "

    show examiner at right

    E "I’m the physical examiner here. You will take off your clothes, be fully examined, and then put on your penitentiary clothes."

    "The woman offers no introduction at this point. You take off your clothes, and the examiner does many checks on you with his instruments, examining your body. "

    E "This one is in healthy condition."

    "He then uncertainly hands you back your original clothes."

    E "(in a loud whisper to Warden Wood) We don’t have any more uniforms fit for a female yet."

    E "Mrs. Blundin here will sew your admission number on your clothes later."

    show blundin at left

    "The woman standing in the corner nods and smiles. During this process, two other men had been walking in a circle around you, jotting down information about your physical appearance. Occasionally, they ask you questions about your birth place, trade, and so on."

    show larcombe

    "The examiner gestures to another man standing in the room. It’s Thomas Larcombe, the penitentiary’s moral instructor. He has been studying you and writing notes the whole time you were being examined."

    TL "Now what was your religious instruction like? Can you read? Write? Tell me what those words say (He points to “Cat,” Cow,” “Mother,” “God” on a paper)"

    TL "I see you poisoned your husband. Now, a successful marriage is the key to all moral and religious redemption, and as a wife you have an obligation to your husband to uphold this. Why did you commit this heinous crime? Are you ready to ask God for forgiveness? "

    "He carefully writes down your stuttering responses."

    hide larcombe
    show warden

    "The warden, Samuel R. Wood, who has been standing in the corner with the woman, now approaches. He looks you up and down with disdain. He carelessly gestures to Mrs. Blundin. "

    SW "Take her to her cell now, Mrs. Blundin."

    hide warden
    hide blundin
    hide examiner
    scene black

    "Mrs. Blundin moves forward and blindfolds you. She takes you by the arm, and begins to lead you through a series of hallways. At one point, you feel the cool air on your face, and realize you have gone outside."

    "You feel yourself crossing the threshold again, and hear Mrs. Blundin’s raucous laughter and what seems to be some of the guards making lewd comments at her. Finally, you both stop and your blindfold is removed."

    jump adjust

# Hinson Scene 3

label adjust:
    scene cell_intake
    with fade
    pause 2.0

    "As your eyes adjust to the dim light, you look around you and see that you’re in a cell. Mrs. Blundin is inside with you, tidying up around you. There’s a bedframe with a mattress on it and a toilet.
     It looks like this cell has not been touched since the last inmate."

    "Through the open door, you see the cell across from you is also open. A woman lounges in there, staring at you."


    show hinson at center
    with dissolve

    AH "You must be new here. I’m Anne Hinson. This is the part of the prison they like to call the “ladies corner.” It’s really just a bunch of decrepit cells at the end of block two that they shove all of us women,
        because they don’t know what else to do with us."

    show hinson at right
    with dissolve
    show blundin at center
    with dissolve

    "Mrs. Blundin laughs. She takes a sip from a pouch hung around her waist that you never noticed before."

    B "One of my jobs around here is to take care of you women. And I don’t get paid, either!
     *grumbles* Because no one wanted to spend money on anything professional when it comes to female inmates."

    B "So you’re going to be helping me with the washing and with any other tasks that I ask you to. And we also have fun here."


    "She winks and offers you her pouch. You’re taken aback, but eagerly reach for it. Anne cheers you on, and you hear a few more whoops from the cells around you."

    "Do you take a drink from the pouch?"

menu:
    "Yes":
        jump Yes
    "No":
        jump No


label Yes:
    "The other women cheer you on and support your action as a “'rebel.'"
    jump Anne

label No:
    "You see some disappointed looks, but Mrs. Blundin makes a comment about how you will come around eventually."
    jump Anne

label Anne:
    hide blundin
    show hinson at center
    with dissolve

    AH "Alright. Ok, that’ll be Amy Rogers, Henrietta Johnson, and Eliza Anderson. Amy and Henrietta’ve been here the longest,
       and then me and Eliza came in here December 1831, and we’ve been here for almost 2 years now."

    AH "I don’t stay in this cell often anymore,
       since Mrs. Blundin helped get me accomodation in the newest block, cellblock four.

        You’ll learn soon enough, it’s easy to get away with a lot here, being female and all."

    show hinson at right

    with dissolve

    show blundin at left

    "She saunters away, slightly swaying. Mrs. Blundin locks your cell with a wink and a wave, and follows Anne."


    pause 1.0
    scene hallway
    with fade


    "You spend a lot of your time in your cell, praying and sleeping."
    "You’re allowed some needle and thread, but mostly that’s just to help Mrs. Blundin mend clothes."

    "She takes you to the washingroom with her, where she puts you and the four other women inmates to work. It’s a fun job, and all five of you are usually drunk. "


    "Mrs. Blundin tells you about all the trouble she gets up to, stealing food from the prison kitchen and supplies stories. She sometimes shares those items with you and the other women. "


    "She tells you all the gossip about the men who work at the prison.
     Often you wash the undergarments of the men who work at Eastern State, and the women titter about how Wood has venereal disease. Mrs. Blundin jokes that she gave him it in an act of defiance."

    "In time, you decide to...."
menu:
    "Get closer with the other women and develop a more rebellious attitude":
        jump Time
    "Distance yourself from the women somewhat as you do not act the same as they do":
        jump Time


label Time:

    scene hallway

    show blundin
    "Mrs. Blundin sometimes has you all aid her in her kitchen theft, under the guise that you are all assisting her in cooking or preparing food.
     Sometimes she takes you to the warden’s office with Anne, and you dress up in his clothes and sit at his desk, making fun of him. "

    hide blundin
    show warden

    "The warden, the moral instructor, and even the guards seem to leave all of you alone, most of them just not really knowing what to do with you all.
     Much more than the male inmates, you seem to disrupt the solemnity of the penitentiary. "

    hide warden
    "More time passes and you to debate whether to tell the Warden or guards about the theft or help Mrs. Blundin"
menu:
    "Help Mrs Blundin":
        jump Rebel
    "Tell the guards or Warden":
        jump Rules

label Rebel:
    "You become more rebellious and close with the other women, you can think of them as actual friends at this point."
    jump party

label Rules:
    "They laugh in your face and don’t believe you and scold you for not focusing on trying to cleanse yourself of sin rather than blaming others for sinning."
    jump party

# Hinson Scene 4

label party:

    scene black

    "Two weeks later. . ."

    scene cell
    with fade

    "Mrs. Blundin bustles over to your cell and unlocks it. Anne is right behind her."

    show hinson
    with fade

    AH "Tonight we're gonna have a party!"

    AH "Me and Eliza are getting out soon, so this is a BIG celebration."

    AH "We’re gonna be “working,” the party tonight, which will have outside
    guests — Mrs. Blundin’s friends and some of the people who work here —
    but it’s the same as us working on washing out venereal disease from clothes."

    AH "We’ll have fun."

    hide hinson
    with fade

    scene basement

    "You walk with Mrs. Blundin to the front of the prison and down stairs \
    into a basement."

    # some characters showing and fading here would add a lot

    show court_blundin
    show leg1 at right
    show baen at left

    "There’s already a lively party going on, lit by candles. Many men. Eliza \
    and other women, all bearing their inmate numbers, hand out food to guests, \
    take big swigs from bottles, and laugh and talk raucously."

    hide court_blundin
    hide leg1
    hide baen

    "It’s chaos, but everyone seems to be having fun."


    show hinson

    "Anne, who’s dressed in different clothing without her prison number — \
    likely given to her by Mrs. Blundin — goes right to a stool, and takes up a \
    fiddle on the floor, and begins to play loudly."

    scene stairs

    show demmy
    with fade

    "You look over to the stairs and see a man with sawdust chips in his hair, \
    likely the carpenter on a late shift, look around the room in wonder."

    hide demmy
    with fade

    "He quickly disappears back up the stairs."

    scene basement
    show hinson

    "You think that Wood will come down, and shut the party down, but nothing \
    happens."

    menu:
        "You see Anne waving you over, an extra fiddle in her hand. She must've \
        remembered the story you told about how you used to play."

        "Go over and join the fun.":
            "You smile and stride over. This is Mrs. Blundin's party - the only \
            reason Wood would show up is if he was a guest."

            "You take the fiddle, and the two of you play to your heart's \
            content. Although, after a few rounds of drinks with the girls, \
            who knows how good you sound."

        "You can feel Wood about to show up at any minute. You just want to get \
        through this night without getting into trouble.":
            "You pretend you didn't notice her. You know you can't get out of \
            this without Anne saying something the next day, so you lean back \
            against the wall nearest the door, prepared to run if there's any \
            trouble."

            "Still, the others come along with the bottle, and, despite your \
            misgivings, you wind up sharing a few more drinks than you planned."

    "The party goes late into the night."

    "By the end you’re so exhausted and drunk that you and Anne dance around \
    the whole prison, fall asleep on the floor, and only creep back to your \
    cells in the early hours of the morning."

    scene cell

    "You don’t see Mrs. Blundin until many hours later, when you’re woken from \
    your hungover slumber to the sound of Mrs. Blundin locking up your cell."

    show blundin

    "She winks when you open your bleary eyes, and you hear her footsteps recede."

    jump discharge

# Hinson Scene 5

label discharge:

    scene hallway
    with fade

    "December 16, 1833."

    "Anne and Eliza were supposed to have been discharged five days earlier."

    "As Anne had told you before, she was supposed to only be in Eastern State for two years."

    "When her discharge date came, however, she was told she couldn’t leave \
    because she had to pay $100 in bail. You heard her and Mrs. Blundin talking \
    angrily together, Anne crying."

    show warden

    "Warden Wood walks by and they get quiet, but Anne is still sniffling."

    "Mrs. Blundin hikes up her skirts to show her ankle and winks at Wood, and he walks quickly away."

    hide warden
    show hinson at right

    show blundin at left

    AH "This is just another measure to dampen my free will!"

    B "Wood is going to want to get you out quick, you know. There’s been \
    whispers all around here of a big investigation on the way people are \
    punished."

    B "He wants you to disappear off these records!"

    hide blundin

    "Mrs. Blundin was right. Later that day, you’re notified by another female \
    inmate in the washroom that Wood had gotten the bail taken care of, and \
    Anne was gone for good."

    jump rumors

# Hinson Scene 6

label rumors:

    scene hallway

    "For a little while at the start of 1834, you’re one of the only female \
    inmates."

    "However, a woman will be admitted today. Mrs. Blundin has told you, and \
    you’re excited to meet her."

    "You hear more whispers about the investigation, and the name \
    “Mr. McElwee” repeated. When you’re working in the kitchen and washroom, \
    you sometimes see him walk by in deep talks with the warden or other male \
    workers."

    "Mrs. Blundin jokes about the investigation, cursing McElwee and the rest \
    of the workers."

    show blundin

    B "Why didn’t that sniveling man ask me for my testimony?"

    B "Why, I oughta go up and flog that damn Quaker son of a bitch Wood for \
    spreading rumors about me!"

    "You smile, take a swig of your contraband alcohol, and take out an apple \
    you swiped earlier from the kitchen."

    menu:
        "Do you want to see the prison through McElwee's eyes, or proceed to \
        the hearing about Mrs. Blundin's behavior?"

        "Join Thomas McElwee on his tour":
            jump mc_intro

        "Proceed to the Hearing":
            jump hearing

# McElwee Storyline

label mc_intro:

    scene esp

    "The year is 1834 in Philadelphia, Pennsylvania."

    "It has come to light that there are complaints circulating regarding the \
    management of Eastern State Penitentiary and the inappropriate behavior of \
    those who work and live there."

    "The state attorney general has convened a joint committee of the legislature \
     to inquire into ESP affairs and investigate the charges made concerning the \
      immoral conduct at the prison, which has only been operating for five years."
    show mcelwee
    with fade

    "You are a notetaker assigned to the task of assisting state legislator Thomas McElwee, one of the five members of the committee, in gathering testimonies. Mr. McElwee has been in Philadelphia for a few weeks before sending for you."

    scene esp_front
    with fade

    "You are instructed to meet him outside the prison gates on Fairmount Avenue."
    "As you walk up to the gates, you are suddenly struck by the immensity of the structure and by a feeling of awe."
    "You stand up straight, take a deep breath, and wait for Mr. McElwee to appear."
    "You see a line of prisoners being escorted into the massive complex, and are surprised to note one woman among them."
    show mcelwee
    TM "Hello! I am glad that you had a safe trip to Philadelphia."
    TM "I hope you are ready and feeling equipped to aid in the collection of testimonies today."
    TM "This prison is in dire need of restructuring and those who are within it are poisoned by its reputation and ability to encourage reform and repentance in the lives and souls of the poor criminals who hope for redemption and penitence."
    TM "In your work for today, take special care of noting any mention of a Mrs. Blundin, the wife of the underkeeper."
    TM "I fear she may be the source of the licentious issues plaguing this magnificent institution and preventing it from reaching its full potential and achieving its mission."
    hide mcelwee
    "\"Thank you, Mr. McElwee. I am ready to begin assisting you and carefully record testimonials.\""
    show mcelwee
    TM "Allow me to escort you inside and I will have the warden, Mr. Samuel Wood, give you a tour before we begin our investigation."

    scene mc_wood

    "You walk through the gates with McElwee at your side. You feel relieved that you are not among the prisoners awaiting inspection and a sentence of isolation."

    scene rotunda

    "A guard escorts you down a long corridor, and you reach the central surveillance rotunda, where Warden Wood is waiting."
    "Standing in the rotunda, you spin around and peer down each row of cell blocks."
    show warden:
        xalign 0.15
    SW "Welcome to Eastern State Penitentiary, also known as Cherry Hill."
    SW "The building was designed by the architect John Haviland, who modeled the structure after the panopticon design. The design of the building allows guards to see down each corridor of cell blocks and monitor prisoners at all times."
    SW "Haviland also relied on inspiration from church architecture to create an aesthetic and environment that encourages penitence and religious devotion."
    "\"How many prisoners are in each cell?\""
    SW "Here we employ the separate system. We believe here that reform can only truly happen when prisoners are in complete isolation."
    SW "They are kept in solitary confinement, and even exercise in a private yard attached to their cell. Because the inmates are seperated, they will not influence or corrupt each other."
    SW "They speak to no one other than the guards and are referred to by numbers rather than their names."
    SW "The prisoners do interact with a religious instructor, Thomas Larcombe, who has been working here since 1831. He guides the prisoners’ moral journey."
    "\"I saw a female prisoner being admitted this morning. How do they factor into this system?\""
    SW "Let me assure you that our institution does everything to support and reform these women and we are handling their transition very well."
    "He puts his hand on your shoulder and, in a more quiet tone, says:"
    SW "As I’m sure you will come to see, it is not my leadership or the prison system that should be under investigation, but might I suggest you pay close attention to any mention of Mrs Blundin."
    SW "She is a gross and power hungry woman, who has taken advantage of these poor women and is poisoning the system which is supposed to help them."
    show mcelwee:
        xalign 0.85
    TM "Yes, I do question Mrs. Blundin’s role in the affairs that have transpired…"
    TM "I myself have heard some of the most vile things about her behavior. Utterly deplorable and despicable if they prove to be true!"
    SW "But, you should form your own opinion first. I hope that all with whom you speak to will give you a similar, and of course accurate, account of our prison. With that, I leave you to your investigation."

    scene yard

    "You walk with Mr. McElwee down one of the corridors until you reach a yard."
    show demmy:
        xalign 0.85
    "There, you encounter Mr. Charles R. Demmy, your first interviewee."
    show mcelwee_right:
        xalign 0.15
    TM "Mr. Demmy, in our last conversation you were speaking about the nature of punishment in the prison. Can you once again introduce yourself for the record before continuing?"
    CD "Yes, of course."
    CD "I am a minister and member of the Prison Society. I often visit inmates at the Eastern State Penitentiary. I was welcomed by Mr. Wood, a man I hold in high regard."
    CD "When I first began my visitations, I believed this system would be extremely cruel. After spending time within these walls, and observing the progress of the inmates, I was proven wrong."
    CD "This system is most remarkable."
    "\"I am very unfamiliar with how prisoners are disciplined in this institution. Can you speak to that? Are prisoners tortured here?\""
    CD "I believe that any method of punishment used has been aptly chosen by the guards and Mr. Wood. From my knowledge, food deprivation is the choice of discipline in the penitentiary, but I know of cases in which a straitjacket was used."
    CD "However, this was a necessary course of action given that the prisoner was insane. I have no doubt that the system employed here and the leadership of Mr. Wood has been beneficial to the lives of the prisoners."
    "After hearing Demmy’s testimony, you decide that something seems off. You thought that this was supposed to be a humane institution… You attempt to question what he has said, however McElwee interrupts --"
    TM "Thank you very much, Mr. Demmy."
    TM "Your testimony has been recorded by my assistant."

    scene rotunda

    show mcelwee_right

    "You walk with McElwee back towards the rotunda and see a man stepping out a cell with a guard present. McElwee recognizes the man and calls him over to you for questioning."

    show coates:
        xalign 0.85

    TM "This is Dr. Benjamin Coates, private physician to Mr. Wood. He often visits prisoners here as well and is also a member of the prison society."
    TM "Hello Dr. Coates, do you mind speaking with us about Mr. Wood’s leadership at the prison, as well as the general state of affairs here?"

    BC "I will have to be quick, but I can spare a few moments. As his personal physician, it is important to me to speak honestly on behalf of Mr. Wood, as he has been one of the best men I have known in my life."
    BC "Under his management, the souls here are quite comfortable and never face cruel punishment. And off the record, he has never had the venereal, though rumors may have you believe otherwise."

    TM "Very well, thank you for your time doctor."

    hide coates
    hide mcelwee_right

    scene rotunda

    show mcelwee

    "As the doctor walks past you, you and McElwee take note of the guard who was accompanying him. McElwee seems to recognize him."

    show baen:
        xalign 0.15

    TM "Ah, Mr. William Baen, do you mind if we walk back with you to the central rotunda and ask you a few questions about life here at the penitentiary?"

    WB "Yes sir, you may. I have actually recently remembered a few things that I would like to be noted in my sworn oath."

    "\"How long have you been employed here?\""

    WB "I have been working as a keeper since 1832, maintaining order and occasionally assisting in disciplining the inmates. It was Mr. Wood who appointed me."

    TM "When we last spoke, you mentioned Mrs. Blundin’s questionable behavior. Can you elaborate today? I have heard that she was often drunk and exhibiting lewd actions."

    WB "Yes, I have seen her intoxicated only once before. As I can recall, it was the morning after a party. While I never once saw her drink liquor, I still will say that she was definitely drunk, though this was the only time I saw her in that state."

    TM "Have you ever seen a convict in a drunken state?"

    WB "Once I saw a female convict intoxicated. I think she went by the name of Anne. It was Mrs. Blundin who revealed to me that she was drunk."
    WB "I remember that this prisoner was locked in my cell block at night."

    "You and McElwee begin to walk away. Suddenly, Baen calls out…"

    WB "I have heard from others that Mrs. Blundin has been known to steal from the prison, property of the state!"
    WB "I myself have seen her steal stockings and a lamp from prison supplies!"

    TM " I see. Thank you for your observations."

    scene yard

    show mcelwee:
        xalign 0.15

    "You and McElwee again decide to walk outside to examine the walls during a moment of leisure. You realize that the prison is still under construction and you observe a few laborers working on a cell block. McElwee points to one of them."

    TM " See that man over there? That is Eugene Faley, a carpenter. I took his testimony a few days ago. It’s quite interesting what he told me."

    "\"Oh, what did he say?\""

    TM "Well, as I can recall, I swore that he had never seen Blundin drunk and she was always an upright kind of woman. He did mention that he attended a party she hosted and saw a black woman playing the fiddle, though he never saw any prisoner at the party."
    TM "Strange indeed, and quite contradictory to some things I have heard. But let us continue with today’s tasks."
    TM "Soon there will be a trial to sort this out once our report is complete. I am aware that an old inspector of the prison is visiting today and I want his account of the goings on here."

    scene scene6gate

    "You and McElwee walk along the walls back towards the center gate and you see a man entering the prison. McElwee points him out as Benjamin Richards, a previous inspector of the prison."

    show mcelwee_right:
        xalign 0.15
    show richards:
        xalign 0.85

    TM "Hello Mr. Richards, this is my assistant for the next few weeks. Would you mind once more repeating your impression of the prison for the record?"
    TM "Can you speak to how the prisoners are treated here?"

    R "From what I have seen, this system is a success. The prisoners hold Mr. Wood and the keepers in high regard, and their actions are never cruel."
    R "I myself have little history with the warden but it seems that this institution is flourishing under his leadership, if certain parties of course did not threaten it."

    TM "Would you care to elaborate who exactly these “parties” are?"

    R "Ah, yes. It was Mrs. Blundin in particular who I thought should be removed from the prison, but alas Mr. Wood insisted she stay."
    R "I personally believe she has soiled the reputation of this penitentiary and has threatened the reformation of any prisoner she has been in contact with. Now if you would excuse me, I must be going."

    hide richards

    "He walks off towards the main rotunda while you and McElwee are left alone."

    "\"Sir, would it be possible for you to explain to me more about the conduct of this Blundin woman? It seems like there are gaps in what exactly I know of her.\""

    TM "Well, I can go back and show you some of the other testimonies I have recorded in your absence. The behavior of this woman really is quite shocking."
    TM "From what I have previously gathered, it is apparent that she made use of both male and female prisoners as workers. She was especially fond of this one woman, Anne Hinson, who played the fiddle at her parties."

    "\"That seems highly unprofessional...even dangerous.\""

    TM "Exactly! The purpose of this separate and silent system was to curb interactions between convicts so they would not influence each other with their evil ways and inhibit reform through God and penitence."
    TM "She made that impossible for them. Can you believe that I have also heard testimonies in which witnesses have stated that Mrs. Blundin had given alcohol to inmates? Well, that’s not the end of it."

    "\"I am in shock. To think a woman of her status should impede the rehabilitation of those wretched criminals...\""

    TM "Apparently, she instructed an inmate on how to escape the prison and even offered him the company of Anne Hinson, before making sexual advances herself. Utterly inappropriate."
    TM "I find it difficult to mention the next set of accusations, they are almost too grotesque to repeat. It has been reported to me by multiple witnesses that Mrs. Blundin has carried out numerous affairs with different employed persons here at the prison… including Mr. Wood!"

    "\"My god, I can’t imagine a member of the fairer sex acting in such a manner!\""

    TM "I speak true! The foreman of the carpenters has relayed that he has seen Mrs. Blundin together with Mr. Wood in his bedroom. It has also been reported that she was in the bedroom of the carriage driver! Is any bedroom free of Mrs. Blundin?"
    TM "In addition to this depravity, she admitted to passing venereal disease to her husband! It is clear that Mrs. Blundin’s foul spirit and corrupting presence are responsible for the issues plaguing this institution."

    "\"This has been enlightening. It is hard to believe that those statements about Mrs. Blundin could all be true, but I suppose the characters of the men who run this institution speak to the integrity of their testimonies.\""
    "\"We have to trust that the hearing and joint committee will find the truth in this terrible situation and handle it accordingly.\""

# Scene 7 - The Hearing

label hearing:
    scene sepia

    "It's the day of the hearing, and it has been extensive."

    "You, along with several other recently released inmates and onlookers, sit behind McElwee, who addresses the legislature. On the left of McElwee, resembling a jury, the men from whom McElwee extracts testimonies against Mrs. Blundin."

    "Mrs Blundin, sits in the witness booth awaiting the further assassination of her character."

    show mcelwee

    TM "Dr. Leiber, who has labored with great assiduity and sound judgement in the cause of “prison reform,” says:"

    TM "“The principle of the Pennsylvania system is solitude with labor.”"

    TM "Solitude prevents contamination of a prisoners mind into a more hardened criminal form. Solitude forces reflection; it is the most powerful moral medicine. Solitude prevents his knowledge by fellow inmates; he has a far greater chance of an honest living."

    TM "Solitude enables transition for a life of criminal excitement to one of stern sobriety. Solitude prevents his finding himself in degraded company. This institution has spat in the face of solitude."

    TM "Speak, Samuel Wood, tell the legislature what you have told me."

    hide mcelwee
    show warden:
        xalign 0.15

    SW "Her actions are universally reviled across our institution. Her improper deportment and practice are entirely unbecoming of her sex and condition. She has defied all notions of respectability."

    SW "She is a deplorable woman, who violated the codes of gender and class refusing the role of a demure and domestic wife. Blundin has corrupted all the men and women of this institution. May God forgive me and my brothers: this wretched witch has made us sin."

    "All the other male characters mumble in accordance with the Warden."

    hide warden
    show leg1

    leg1 "Alas, Mrs. Blundin seems to be a sour grape in this benevolent project. For the good of the Eastern State Penitentiary and the even greater good of the Commonwealth of Pennsylvania, I recommend Mrs. Blundin be dismissed."

    hide leg1
    show leg2:
        xalign 0.35

    leg2 "We must prevent the future impropriety. I propose more stringent separation between the two sexes. Furthermore, there shall be no needless frolicking around the prison."

    hide leg2
    show leg1:
        xalign 0.70

    leg1 "I echo these sentiments."

    hide leg1
    show leg3

    leg3 "Mrs. Blundin’s evil must wreak damage no further. The boundaries of prison morality must be stopped from dissolving. The reemergence of subjectivity must be curbed."

    leg3 "The private should be prevented from intruding the public space. All employees must be forced to uphold the protocols of the institution."

    hide leg3
    show leg1:
        xalign 0.70

    leg1 "I recommend Mr. Wood assert his authority. Your prisoners; time out of cells must be limited to absolute and unequivocal necessity. The project MUST be implemented in its full and pure form."

    hide leg1
    show court_blundin

    "After a few more measures are imposed  the inquiry is closed."

    scene black

    "This game was made remotely by ten University of Pennsylvania students over four weeks in March-April 2020. We invite you read some of our conclusions and reflect on the game by click on {a=https://espwomen.hcommons.org/conclusions/}this link{/a}."

    return
