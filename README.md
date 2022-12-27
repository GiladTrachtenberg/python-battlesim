# Python Battle Simulator 

Hello everyone! Here, I'm showcasing a very nice (and niche) project coded in Python; a battle simulator. In general, it takes into account 5 tiers of soldiers, and divides the army into mounted (cavalry), ranged (archers) and infantry. It takes into account more variables and multipliers such as morale (commander_multiplier), terrain advantage, strategic advantage and more. We've We'll dive in a bit deeper shortly.

## The basics - how do I even run it? What do I do

- **First** and foremost, you'll need to have [Python 3.7 or higher](https://www.python.org/downloads/) installed on your computer (added a link for your convenience).
- **Secondly**, you might want to browse the code and update some of the variables, multipliers and values youreselves. 
- **Lastly**, simply run the code via your preferred IDE (or shell) and see the results for yourselves! If you're using a shell to run it, make sure to navigate to the file and run it in a similar fashion to what's shown here: ```python3 ./battlesimulator.py``` (make sure to customize this, if needed, according to your shell).

Regardless, it's important to denote (at this early stage of the documentation) that this battle simulator might be "*inefficient*" in terms of pure computational context, as it performs its simulaton on a soldier by soldier basis. Don't worry if you don't fully understand it now; you'll understand it the deeper we'll dive into the documentation. 

## The Nitty-Gritty; "Tell me, what the hell have you done?!"

Easy, now! I'll be right happy to, of course. Just a little something to note down before we proceed to the truly fun stuff. When you see variables/arguments called "attacker" and "defender" sent to a funciton, remember that these are troops who are positioned on this side. For instance, an archer attacker and a cavalry defender.

### The Basics - Lesson 1: The Main Dictionaries

To initiate the code we start off with three main ***dictionaries***. One named "*SOLDIERS_ATTRIBUTES*", another called "*CLASS_ADVANTAGES*" and lastly "*TERRAIN_ADVANTAGES*". The **class advantages** pertain to the fact that certain troops have certain advantages over their adversaries. I.e, archers have a ranged advantage, but when infantry/cavalry get close, their edge turns into a disparity. 

-**Q**: "*Tell me, why three main dictionaries? Why not use just one? Why not a simple list? Or an array?*"
-**A**: Well, the answer to that's quite simple. It's more plain and more efficient (in terms of readability and personal comfort - there is no real benefit doing either thing in terms of computation efficiency on this scale). 

***Moving on***, you can see that these dictionaries are composed of several items that contain different values. Some are *metric stats* such as the health quantity, and others are variables that pertain to items, such as the preferred distance. 

### The Basics - Lesson 2: The 'calculate' Functions

The calculate functions are like the heart of this program, due to the fact that they perform the most viable, critical computations relevant to the simulator. Or, in other words - they do most of the simulation. Both the "**calculate_attack**" and "**calculate_defense**" functions operate very similarly; measure how much of them was actually dealt to the enemy. They work by taking all of the multipliers/variables into consideration (terrain, class advantage, etc.). 

Conversley, the "**calculate_distance_multiplier**" has a bit more to it than simply taking multipliers into account, as you can see. Firstly, it draws the preferred distance of the troop (i.e long range for archers) from the relevant dictionary section. Second, it equates it to the other side; if it is equal, there's no advantage to either side (i.e both tier of archers and the same amount of them fight on an even field at their **preferred distance**). Otherwise, it deviates in favor of the triumphant (in that regard) side. 

### The Basics - Lesson 3: The 'Battle' Function

The battle function is like the brain of the function, given it mostly does the orchestration of the simulation using the 'heart' which is the '***calculate***' function. To explain this more plainly, I'll be using a list to better illustrate the meanings behind each segment of this function:

- Firstly, it calls the "**calculate_distance_multiplier**" to do its task.
- Secondly, it calculates the class advantage by pulling the relevant values from the *CLASS_ADVANTAGE* dictionary and comparing them to their enemies. 
- Thirdly, it calls the "**calculate_attack**" and "**calculate_defense**" functions to perform the necessary (and aforementioned) calculations.
- Moving forward, it substracts the defense value from the attack damage perfromed in the previous step to see how much damage the attacked party was actually taking. If the value is smaller than 0, it zeroes the value, as it is not possible to take zero damage, naturally. 
- Next, it subtracts the taken damage from the attacked's health quantity (remember the first dictionary?).
- Lastly, if the damage taken depletes the health bar of the attacked, we can say that they are defeated. Otherwise, they're not.

### The Intermediate Course: 

What do we do next? Well, we need to organize some composition. Or in other words, we need to field an army. As this is a very plain simulator, I've given fixed values; but of course, as the simulator is improved, this will have dynamic values and perhaps even a cozy UI interface allowing for quick selections. 

So we organized two armies; and before I reveal the answer, try and guess who will win based on the provided values yourselves :)

Once we've organized them, we're ready use other advantage variables, such as the terrain and the technical (pertaining to used weapons), as well as the **commander_multiplier** which refers to a morale and organizational boost received from the sheer fact of having a commander in charge of your force.

What's next? Well, you're about to graduate. 

### Master of War

At last, we've arrived at what we commenced for; the simulation itself. Without further ado, let's break it down:

- Using my favorite loop - a *conditional "*Whilte True*", we lay the foundation for our simulation. 
-**Q**: "*But wait. What is a conditional "while true" loop? Isn't a while=true loop supposed to run indefinitely, while something is true?*"
-**A**: Well, not necessarily. You see, even if a while loop is true, we can force it to break the loop, under *certain, special conditions*. How? For that, the amazing C language (which Python compiles into) invented such a "*special condition* known as the break statement. More on it [here](https://learn.microsoft.com/en-us/cpp/c-language/break-statement-c?view=msvc-170/). So in our case, we repeat this statement under certain conditions, which we will explore shortly.
- Moving on, we now assign random attributes from the army we composed to troops. Of course, it happens randomly.
- Using these random attributes, we conduct the fight between the troops by calling the **battle** funciton which uses the variables we mentioned earlier. As previously mentioned, the **battle** function is the computation behind the simulation, or in other words; the simulation itself. 
- Then it verifies the following; if someone is defeated, their count is lowered by one in accordance with the relevant troop (remember; it does so on a troop vs troop basis). If either army has been defeated, it simply ends the fight. Then, it prints the results. 

## With that, we come to an end. As time passes and based on traffic, I'll include a Q&A as a separate section of this readme file. Until then, keep on codin'!

### LICENSE

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/GiladTrachtenberg/python-battlesim/main/LICENSE)