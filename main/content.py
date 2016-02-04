act1 = {'intro': {'intro': "<h1 id='header'>Welcome to the game of fabulous adventure!</h1><br><br> \
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
                    <button class=\'sexform\' name='general' action='begin'>Continue</button>"},

        'general': {'begin': '<p>{charname} stands at the doorstep of a dilapidated old inn, the first sign of civilization {heshe} has seen for many days of travel  \
                      through wild and strange lands. Rain is falling in relentless sheets out of the impenetrable darkness of the night. Though the inn barely looks habitable, \
                      {charname}\'s heart soars with relief at the site of warm light oozing from the windows, and {heshe} can even discern the familiar sounds of a friendly tavern \
                      from behind the door. Squinting up through the rain, {heshe} can barely read the rickety old sign hanging over the door: "Frosty Swath".  \
                     \
                     <button class=\'action\' name=\'general\' action=\'questions2\'>Continue</button>',


                    'questions2': "<fieldset class='wealthform'> Let me ask you a couple questions about your character, {charname}...<br><br> How wealthy is {charname}?  \
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
                      <button class=\'wealth' name='general' action='questions3'>Continue</button>",

                    'questions3': "<fieldset class='form'> How tall is {charname}?  \
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
                      <button class=\'form_but\' name='general' action='questions4'>Continue</button>  ",

                    'questions4': "<fieldset class='form'> How is {charname} built?  \
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
                    <button class=\'form_but\' name='general' action='begin2'>Continue</button>",

                    'begin2':"<p>Gazing up at the sign, {charname} thinks to {himselfherself}, \"Frosty Swath. Yes, this is the place.\". <br><br>{Cheshe} reaches a hand to the door.  \
                      Whispering a silent thanks that {heshe} made this god forsaken journey in one piece... made it this far at least, {charname} grasps the doorknob...</p>  \
                      \
                      <button class='action entry' genAct='look' name='general' action='entry1' header='General Actions'>Continue</button>",

                    'entry1': "<p><br><br> It was a usual night at the Frosty Swath. The tavern hall was a long dim room, filled with tobacco smoke and the raucous murmurings \
                    of drunken conversations. For a lone inn on a strange dark road leagues from any civilization, it was surprisingly busy. What was even more curious \
                    was the variety of folks populating this ramshackle affair on a 'usual' night. Most of the patrons appeared to be roughened outdoorsman types.  \
                    Neither farmers nor aristocrats were present. But there was an abundance of straggly beards and weather stained coats.<br><br> The inn is surprisingly busy for a couple \
                    reasons. Firstly, it is the only building at a major crossroads. Also, it has recently come to light that the inn is situated very closely to some mysterious ruins and \
                    happenings. <br><br>  \
                    The constant murmer of conversation abruptly ceases when the front door flies open, partially propelled by a gust of wind and rain, but immediately followed by a dark \
                    figure who quickly steps inside and slams the door shut. The figure is wrapped in a soaking wet \
                    \
                    [{'wealth_rich':', but fine travelling cloak. Many of the inn patrons note the fine embroidery along the hem. The newcomer obviously had some coin.', \
                    'wealth_average':', and weather-stained travelling cloak. ', \
                    'wealth_poor':'travelling cloak. Though \"cloak\" was a bit of a stretch. It looked more like tattered rags, and the individual was obviously destitute. '}] \
                    \
                    Through the folds of outerwear, the person appeared to be \
                    \
                    [{'height_tall':'rather tall,', 'height_average':'of average height,', 'height_short':'a bit short,'}]  \
                    [{'stature_robust':'and with an athletic build.', 'stature_average':'and average build.', 'stature_thin':'and thin.',  'stature_fat':'and surprisingly fat. Those of \
                    larger girth were nearly unheard of in these rough parts, and several people chuckled under their breath at this.'}]  <br><br>\
                    \
                    The newcomer reaches up to throw back their wet hood...</p> \
                    \
                    <button class='action' name='general' action='questions5'>Continue</button>",

                    'questions5': "<fieldset class='color_form'> What color is {charname}'s hair?  \
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
                      <fieldset class='style_form'> What style is {charname}'s hair?  \
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
                      <button class='hair_but' name='general' action='questions7'>Continue</button>",

                    'questions7': "<fieldset class='form'> How old is {charname}?  \
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
                    <button class=\'form_but\' name='general' action='questions8'>Continue</button>",

                    'questions8': "<fieldset class='form'> What color are {charname}'s eyes?  \
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
                    <button class=\'form_but\' name='general' action='entry2'>Continue</button>",

                    'entry2': "<p>...revealing [{'age_young':'a young', 'age_mature':'a middle aged', 'age_middle':'an older', 'age_aged':'an old'}] \
                    [{'male':' man', 'female':' women'}] with [{'hair_short':'short,', 'hair_long':'long,', 'hair_bald':'a bald head.', 'hair_shaggy':'shaggy,'}] \
                    [{'hair_brown':'brown', 'hair_blonde':'blonde', 'hair_black':'black', 'hair_grey':'grey'}] hair. <br><br>  \
                    \
                    From behind the bar, a <u class='npc' header='bartender' name='johnson' action='talk attack' actCont='talk2'>large moustachioed man</u> bellows out, \
                    \"Ho there traveller! Have a seat and wet your whistle.\".</p>",


                    'look': "<p>{charname} scans the room slowly, taking mental note of interesting details as they catch {hishers} eye. Behind the bar, the <u class='npc' header='bartender' name='johnson' action='talk attack' actCont='talk2'>bartender</u> \
                      polishes a tankard absently, looking about the room like an eager bird-dog. Presently someone at the other end of the bar hollers, 'Johnson, another round if you please!' The bearish bartender \
                      tilts his head in acknowledgement, and begins pulling tankards of ale from one of several kegs behind the bar.<br><br> A small handful of local sorts line the barstools. \
                      Nearest to {charname}, a somewhat <u id='reynold' class='npc' name='reynold' header='shabby man' action='talk'>shabby looking fellow</u> eyes {himher} quizzically with a small smile. It's obvious that he's making some appraisal of {charname}. \
                      'Seems like the kind of guy that would buy me a drink', {charname} thinks to {himselfherself}, 'or try and get me to buy him one.', {heshe} chuckles.<br><br>Off to {charname}'s right, at the far end of the hall, a large fire roars \
                      invitingly in a massive blackened hearth. Several plush and haggard armchairs ring the area. All of them are filled with laughing and gasping lookers-on, for, \
                      standing in the middle of the circle of chairs, a rather old and <u id='wilma' class='npc' name='wilma' header='crazy women'>insane looking women</u> appears to be regaling her audience. {charname} can't make out her words over the racket \
                      of the bar room, but her highly spastic and animated contortions indicate that she is in the midst of a wild and fascinating tale of some sort.</p>"},


        'johnson': {'talk': "<p> {charname} saunters right up to the bar and plops {hisher} weary body into a high rickety stool. {Cheshe} thinks it might be the most comfortable damned stool in history.<br><br> \
                      {Cheshe} gives the bartender a polite smile, and says,  \
                      \"I'll have your largest mug of ale sir!\"<br><br> {charname} watches with large eyed anticipation as Johnson produces an absurdly huge metal tankard from under the bar, \
                      and begins pulling a frothy amber ale from one of the kegs behind him. Just as the beer fills to the rim of the mug, he deftly whisks the mug up and over the bar, sliding it roughly onto its pocked \
                      and stained surface, golden suds sloshing over the rim and down the sides. The large man \
                      thrusts a beefy hand at {charname}'s surprised face, \"Name's Johnson, pleased ta meet ya! I run this fine establishment. Where do you hale from stranger?\"",

                    'talk2': "<fieldset class='form'> Where is {charname} from?  \
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
                      <fieldset class='form'> What do you tell Johnson?  \
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
                      <button class='hair_but' name='general' action='talk3'>Continue</button>",

                    'talk3': "<p>TALK</p>"},


        'reynold': {'talk': "<p>  {charname} gives the man a nod, as {heshe} sidles up to the bar and pulls out the next stool. \"Howdy\", he says with a friendly grin, \"what are you drinking tonight? Of course \
                     everyone goes for the ale, but those in the know know to ask for 'ole Johnson's Black Crow.\" He gives {charname} a sneaky grin. Judging by his breath, the man is a legitimate drinker.</p>"}}

