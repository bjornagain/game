act1 = {'intro': {
            'intro': "<h1 id='header'>Welcome to the game of fabulous adventure!</h1> \
                    <p>To play the game, just read the text in this window. \
                    If you see something underlined, that means you can click on it. You'll see some buttons pop up at the bottom of the window. \
                    Those buttons will give you things you can do, with the underlined thing that you clicked on. \
                    Sometimes you'll see buttons pop up at the bottom of the window that aren't for anything underlined.  \
                    These are more general actions you can take. Currently the text output does not automatically scroll down,  \
                    so if you click on something and the text window doesn't change, you probably just need to scroll down to see the new text.  \
                    You can always scroll back up to click on stuff. </p> \
                    \
                    <fieldset class='sex'> Choose your sex  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios1' value='male' checked>Male  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios2' value='female'>Female  \
                        <input type='text' class='form-control' placeholder=\"Enter your character's name, and click Continue.\" id=\"nameform\">  \
                      </fieldset>  \
                    \
                    <p><a class='sexform button' name='general' action='begin'>Continue</a></p>"},

            'general': {
                'begin': ["{charname} stands at the doorstep of a dilapidated old inn, the first sign of civilization {heshe} has seen for many days of travel  \
                      through wild and strange lands. Rain is falling in relentless sheets out of the impenetrable darkness of the night. Though the inn barely looks habitable, \
                      {charname}'s heart soars with relief at the site of warm light oozing from the windows, and {heshe} can even discern the familiar sounds of a friendly tavern \
                      from behind the door. Squinting up through the rain, {heshe} can barely read the rickety old sign hanging over the door: \"Frosty Swath\".<br>  \
                     \
                     <a href='#' class='action button' name='general' action='questions2'>Continue</a>"],


                'questions2': ["<fieldset class='wealthform'> Let me ask you a couple questions about your character, {charname}...<br><br> How wealthy is {charname}?  \
                    <label class='radio'>  \
                        <input type='radio' name='optionsRadios' id='optionsRadios1' value='wealth_rich' checked>Wealthy. This means {heshe} is part of the aristocratic class.  \
                    </label>  \
                    <label class='radio'>  \
                        <input type='radio' name='optionsRadios' id='optionsRadios2' value='wealth_average'>Average wealth. {charname} is not nobility, and has spent {hishers} life working a trade.  \
                    </label>  \
                    <label class='radio'>  \
                        <input type='radio' name='optionsRadios' id='optionsRadios2' value='wealth_poor'>Poor. You are part of the lowest class of society.   \
                    </fieldset>  \
                      \
                    <a href='#' class='wealth button' name='general' action='questions3'>Continue</a>"],

                'questions3': ["<fieldset class='form'> How tall is {charname}?  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios1' value='height_tall' checked>Tall  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios2' value='height_average'>Average  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios3' value='height_short' checked>Short  \
                        </label>  \
                      </fieldset>  \
                      \
                      <a href='#' class='form_but button' name='general' action='questions4'>Continue</a>"],

                'questions4': ["<fieldset class='form'> How is {charname} built?  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios1' value='stature_robust' checked>Robust. Strong, athletic.  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios2' value='stature_average'>Average  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios3' value='stature_thin' checked>Thin  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios4' value='stature_fat' checked>Fat  \
                        </label>  \
                      </fieldset>  \
                    \
                    <a href='#' class='form_but button' name='general' action='begin2'>Continue</a>"],

                    'begin2':["Gazing up at the sign, {charname} thinks to {himselfherself}, 'Frosty Swath. Yes, this is the place.'. <br><br>{Cheshe} reaches a hand to the door.  \
                      Whispering a silent thanks that {heshe} made this god forsaken journey in one piece... made it this far at least, {charname} grasps the doorknob...<br>  \
                      \
                      <a href='#' class='action entry button' genAct='look' name='general' action='entry1' header='General Actions'>Continue</a>"],

                    'entry1': ["It was a usual night at the Frosty Swath. The tavern hall was a long dim room, filled with tobacco smoke and the raucous murmurings \
                        of drunken conversations. For a lone inn on a strange dark road leagues from any civilization, it was surprisingly busy. What was even more curious \
                        was the variety of folks populating this ramshackle affair on a 'usual' night. Most of the patrons appeared to be roughened outdoorsman types.  \
                        Neither farmers nor aristocrats were present. But there was an abundance of straggly beards and weather stained coats.<br><br> The inn is surprisingly busy for a couple \
                        reasons. Firstly, it is the only building at a major crossroads. Also, it has recently come to light that the inn is situated very closely to some mysterious ruins and \
                        happenings. <br><br>  \
                        The constant murmer of conversation abruptly ceases when the front door flies open, partially propelled by a gust of wind and rain, but immediately followed by a dark \
                        figure who quickly steps inside and slams the door shut. The figure is wrapped in a soaking wet",
                        {'wealth_rich':", but fine travelling cloak. Many of the inn patrons note the fine embroidery along the hem. The newcomer obviously had some coin.",
                        'wealth_average':", and weather-stained travelling cloak. ",
                        'wealth_poor':"travelling cloak. Though cloak was a bit of a stretch. It looked more like tattered rags, and the individual was obviously destitute."},
                        "Through the folds of outerwear, the person appeared to be",
                        {'height_tall':"rather tall,", 'height_average':'of average height,', 'height_short':'a bit short,'},
                        {'stature_robust':'and with an athletic build.', 'stature_average':'and average build.', 'stature_thin':'and thin.',  'stature_fat':'and surprisingly fat. Those of \
                        larger girth were nearly unheard of in these rough parts, and several people chuckled under their breath at this.<br><br>'},
                        "The newcomer reaches up to throw back their wet hood...,<br> \
                        <a href='#' class='action button' name='general' action='questions5'>Continue</a>"],

                    'questions5': ["<fieldset class='color_form'> What color is {charname}\'s hair?  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios1' value='hair_brown' checked>Brown \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios2' value='hair_blonde'>Blonde  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios3' value='hair_black'>Black  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios3' value='hair_grey'>Grey  \
                        </label>  \
                      </fieldset>  \
                      \
                      <fieldset class='style_form'> What style is {charname}\'s hair?  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios1' id='optionsRadios1' value='hair_short' checked>Short \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios1' id='optionsRadios2' value='hair_long'>Long  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios1' id='optionsRadios3' value='hair_bald'>Bald  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios1' id='optionsRadios3' value='hair_shaggy'>Shaggy  \
                        </label>  \
                      </fieldset>  \
                      \
                      <a href='#' class='hair_but button' name='general' action='questions7'>Continue</a>"],

                    'questions7': ["<fieldset class='form'> How old is {charname}?  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios1' value='age_young' checked>Young, 17-28 \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios2' value='age_mature'>Mature, 29-38  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios3' value='age_middle'>Middle aged, 39-49  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios3' value='age_aged'>Aged, 50-65  \
                        </label>  \
                      </fieldset>  \
                    \
                    <a href='#' class='form_but button' name='general' action='questions8'>Continue</a>"],

                    'questions8': ["<fieldset class='form'> What color are {charname}\'s eyes?  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios1' value='eyes_blue' checked>Blue \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios2' value='eyes_brown'>Brown  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios3' value='eyes_green'>Green  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios3' value='eyes_grey'>Gray  \
                        </label>  \
                      </fieldset>  \
                    \
                    <a href='#' class='form_but button' name='general' action='entry2'>Continue</a>"],

                    'entry2': ["...revealing",
                        {'age_young':'a young', 'age_mature':'a middle aged', 'age_middle':'an older', 'age_aged':'an old'},
                        {'male':' man', 'female':' women'},
                        "with",
                        {'hair_short':'short,', 'hair_long':'long,', 'hair_bald':'a bald head.', 'hair_shaggy':'shaggy,'},
                        {'hair_brown':'brown', 'hair_blonde':'blonde', 'hair_black':'black', 'hair_grey':'grey'},
                        "hair. <br><br>  \
                        \
                        From behind the bar, a <u class='npc' header='bartender' name='johnson' action='talk attack' actCont='talk2'>large moustachioed man</u> bellows out, \
                        \"Ho there traveller! Have a seat and wet your whistle.\"."],


                    'look': ["{charname} scans the room slowly, taking mental note of interesting details as they catch {hishers} eye. Behind the bar, \
                      the <u class='npc' header='bartender' name='johnson' action='talk attack' actCont='talk2'>bartender</u> \
                      polishes a tankard absently, looking about the room like an eager bird-dog. Presently someone at the other end of the bar hollers, 'Johnson, another round if you please!' The bearish bartender \
                      tilts his head in acknowledgement, and begins pulling tankards of ale from one of several kegs behind the bar.<br><br> A small handful of local sorts line the barstools. \
                      Nearest to {charname}, a somewhat <u id='reynold' class='npc' name='reynold' header='shabby man' action='talk'>shabby looking fellow</u> eyes {himher} quizzically with a small smile. It\'s obvious that he\'s making some appraisal of {charname}. \
                      'Seems like the kind of guy that would buy me a drink', {charname} thinks to {himselfherself}, 'or try and get me to buy him one.', {heshe} chuckles.<br><br>Off to {charname}\'s right, at the far end of the hall, a large fire roars \
                      invitingly in a massive blackened hearth. Several plush and haggard armchairs ring the area. All of them are filled with laughing and gasping lookers-on, for, \
                      standing in the middle of the circle of chairs, a rather old and <u id='wilma' class='npc' name='wilma' header='crazy women'>insane looking women</u> appears to be regaling her audience. {charname} can\'t make out her words over the racket \
                      of the bar room, but her highly spastic and animated contortions indicate that she is in the midst of a wild and fascinating tale of some sort."]},


        'johnson': {'talk': ["{charname} saunters right up to the bar and plops {hisher} weary body into a high rickety stool. {Cheshe} thinks it might be the most comfortable damned stool in history.<br><br> \
                      {Cheshe} gives the bartender a polite smile, and says,  \
                      \"I\'ll have your largest mug of ale sir!\"<br><br> {charname} watches with large eyed anticipation as Johnson produces an absurdly huge metal tankard from under the bar, \
                      and begins pulling a frothy amber ale from one of the kegs behind him. Just as the beer fills to the rim of the mug, he deftly whisks the mug up and over the bar, sliding it roughly onto its pocked \
                      and stained surface, golden suds sloshing over the rim and down the sides. The large man \
                      thrusts a beefy hand at {charname}\'s surprised face, \"Name\'s Johnson, pleased ta meet ya! I run this fine establishment. Where do you hale from stranger?\""],

                    "talk2": ["<fieldset class='form'> Where is {charname} from?  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios1' value='home_roxbury' checked>Roxbury, nearest town back west. \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios2' value='home_shadowlands'>The Shadowlands, far to the east.  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios3' value='home_illium'>Illium, the heart of the great empire.  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios4' value='home_rambler'>Originally? {charname} doesn\'t even remember.  \
                        </label>  \
                      </fieldset>  \
                      \
                      <a href='#' class='form_but button' name='johnson' action='talk3'>Continue</a>"],


                    "talk3": ["<fieldset class='form'> What does {charname} tell Johnson?  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios1' value='home_truth' checked>The truth. \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios2' value='home_lie'>Lie!  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios3' value='home_cagey'>{charname} would rather not say.  \
                        </label>  \
                      </fieldset>  \
                      \
                      <a href='#' class='form_but button' name='johnson' action='talk4'>Continue</a>"],

                    "talk4": [
                        {'home_truth':{
                            'home_roxbury':"\"Humble Roxbury, just ten leagues back west.\"<br>",
                            'home_shadowlands': "\"The Shadowlands, far to the east.\"",
                            'home_illium': "\"Fair Illium, the greatest city in all the Empire.\"",
                            'home_rambler': "\"Oh, I\'m not from anywhere in particular. The great green earth is my home.\""},
                        "home_lie": "{charname} chuckles silently. {Cheshe} is not about to give away information \
                            for free, and casually lies to the barkeep: \"The deepest south sir, from the town of Derby past the Great Marsh.\"",
                        "home_cagey": "\"Id rather not say.\", replies {charname} curtly."},
                        {"home_truth":
                            {'home_roxbury':"The bartender is quick to smile and nod, \"I figured as much, I know a local when I see one. What brings you to the Crossroads?\"",
                            'home_shadowlands': "The large man looks slightly taken aback, and says with a forced smile,\"The Shadowlands huh? We dont see many folks from those parts around here. \
                                Whats your business here at the Frosty Swath?\". His tone is not entirely genteel, and {charname} gets the feeling that Johnson isnt making smalltalk with this question.",
                            'home_illium': "\"Illium! Of course I suspected as much. Your dress and bearing have the mark of a superior class. And what brings you to our humble crossroads?\"",
                            'home_rambler': "Johnson gives a slight roll of the eyes and a knowing smile. Hes being friendly, but of course {charname} is well aware that business proprietors are never excited \
                            to entertain vagabonds. The large bartender is already losing attention, scanning the room with his eyes whilst asking, \"A traveler eh? Well we dont have any work around here these days. \
                            Anything in particular bring you out this way?\""},
                        'home_lie': "The mustachioed man nods quietly, as though thinking, and replies, \"Mmhmm Derby, I\'ve been through Derby, though it was many \
                            years ago. I wouldn\'t have pegged you a Derby person.\"",
                        "home_cagey": "Johnson\'s stare gets a bit more intense, but obviously they get their share of strange characters out here. The bartender shrugs, \
                            \"Very well. So long as you dont cause any trouble we dont turn away paying customers. Wave if you need anything.\"<br><br>"},
                        "<a href='#' class='form_but button' name='johnson' action='talk5'>Continue</a>"],

                    "talk5": ["<fieldset class='form'> Why is {charname} in the Crossroads?  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios1' value='purpose_person' checked>{charname} is looking for someone. \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios2' value='purpose_monster'>{charname} is a monster hunter.  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios3' value='purpose_treasure'>{charname} is a treasure hunter.  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios3' value='purpose_adventure'>{charname} is just passing through, looking for adventure!  \
                        </label>  \
                      </fieldset>  \
                      \
                      <a href='#' class='form_but button' name='johnson' action='talk6'>Continue</a>"],

                    "talk6": [{"purpose_person":"<fieldset class='form'> Who is {charname} looking for?  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios1' value='person_brother' checked>{charname}\'s brother, who was out this way some months ago.  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios2' value='person_criminal'>A dangerous criminal.  \
                        </label>  \
                      </fieldset>  \
                      \
                      <a href='#' class='form_but button' name='johnson' action='talk7'>Continue</a>",

                      "purpose_monster": "<fieldset class='form'> What monster is {charname} hunting?  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios1' value='monster_jabber' checked>The Jabberwock, who art sly. \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios2' value='monster_cash'>{charname} will dispose of any monster, for a reasonable fee!  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios3' value='monster_griffon'>{charname} seeks the griffan of Yorp, to exact {hisher} revenge.  \
                        </label>  \
                      </fieldset>  \
                      \
                      <a href='#' class='form_but button' name='johnson' action='talk7'>Continue</a>",

                      "purpose_treasure": "<fieldset class='form'> What treasure is {charname} seeking?  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios1' value='treasure_chalice' checked>The purple chalice. \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios2' value='treasure_stone'>The seerstone of Zoaraster.  \
                        </label>  \
                        <label class='radio'>  \
                          <input type='radio' name='optionsRadios' id='optionsRadios3' value='treasure_horde'>Old Lord Balkney's booty horde.  \
                        </label>  \
                      </fieldset>  \
                      \
                      <a href='#' class='form_but button' name='johnson' action='talk7'>Continue</a>",
                      "purpose_adventure": "<p>Nothing in particular, outside of good conversation and grand adventure!</p>"}],

                    "talk7": [{
                        'purpose_person':
                            {'person_brother':"\"Im looking for my brother, who was travelling through these parts \
                                three months ago to see his bride to be. We have not heard from him, and he never reached his destination. His name was Stan, \
                                and was roughly yea tall.\". Johnson looks thoughtful, then replies that he did see this person, and X and Y.",
                            'person_criminal':"\"I\'m hunting a dangerous criminal. He goes by many names, including, Tom, Mary, and Dick. Roughly yea tall, \
                                with blonde hair, and a surly stink eye that he cannot hide and cannot be missed.\". Johnson looks thoughtful, then replies that \
                                he did see this person, and X and Y."},
                        'purpose_monster':{
                            'monster_jabber':"\"It is a beast I seek! The sly and brimy Jabberwock, \
                                whose name is not to be spoken\". Johnson raises his eyebrows, smiling slightly. He seems impressed by {charname}\'s statement. \
                                \"I cant help you with that sir. Talk to Reynold over there.\"",
                            'monster_cash':"\"Im a monster hunter, sir! And a braver you shall not find! \
                                Got any work?\". Johnson raises his eyebrows, smiling slightly. He seems impressed by {charname}\'s statement. \"I cant help you with that sir. \
                                Talk to Reynold over there.\"",
                            'monster_griffon':"\"I am hunting a most deadly and sinistre beast, the Griffon.\". Johnson raises his eyebrows, \
                                smiling slightly. He seems impressed by {charname}\'s statement. \"I cant help you with that sir. Talk to Reynold over there.\""},
                        'purpose_treasure':{
                            'treasure_chalice':"\"I seek The Purple Chalice\". \"Mmm, treasure eh? Talk to old Wilma\", Johnson casts \
                                a glance across the room at a crazy hat lady.",
                            'treasure_stone':"\"I seek the fabled seerstone of the great Zoaraster!\". \"Mmm, treasure eh? Talk to old Wilma\", Johnson casts a glance across the room at a \
                                <u class=\'npc\' header=\'crazy women\' name=\'wilma\' action=\'talk attack\' actCont=\'talk2\'>crazy hat lady</u>.",
                            'treasure_horde':"\"I seek Old Balkneys lost hoard!\". \"Mmm, treasure eh? Talk to old Wilma\", Johnson casts a glance across the room at a crazy hat lady."}}]
                    }}






