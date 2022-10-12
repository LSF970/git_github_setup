# Dictionary basics :D

#1 - Define a dictionary call story1, it should have the followign keys:
        # 'start', 'middle' and 'end'
story1 = {
    "Start": "In a world filled with out of control animals, one beast became a man and used his powers to fight the chaos engulfing the world. From the plains of Kenya a young Masai boy got lost. He spent 4 days and 4 nights trudging through the wild landscape, avoiding the hostile wildlife and foraging for food. On the 5th day he was cornered by a Hyena clan. Fearing for his life the boy cried out, for no other reason than to alert any nearby humans. But it was not a human that came to his aid. It was a Rhino",
    "Middle": "The Rhino charge not at the boy but at the ravenous Hyena, showcasing the beast's raw strength and power. Turning to face the shocked boy, the Rhino looked tired. THe boy did not realise it at first but the Rhino was gravely injured. It must have been an injury sustained before the Hyena encounter but the Rhino had used it's last pounce of strength to save him. The boy calmed the Rhino, laying it down on it's side. He couldn't escape the feeling this Rhino had a kind and noble soul, one that deserved to live on. AS the Rhino took it's last breath the boy felt his sadness peak and then fade. All of a sudden he felt different. Proud and noble. He rose to his feet and surveyed the landscape, he was now calm and felt at home. No longer anxious in his surroundings. He noticed the Rhino had dissapeared! No body, no trace of it. Could it all be a dream?",
    "End": "As the boy made his way back to his village he was no longer scared or timid. He stomped through the plains in clear view of the animals he once feared. But none so much as looked his way. After just a few hours the boy found the entrance to the valley his community lay within. However the passage was now blocked. A huge boulder lay in his way. For some reason the boy got incredibly angry incredibly fast. He faelt himself grow larger, his torso deforming and creating muscle he did not have before. After just a few minutes the boy took a few steps back and prepared to charge at the boulder. Just a few hours ago it would have seemed obsurd but now the boy believed fully in his ability to destroy the boulder by charging face first into it. He closed his eyes and to his suprided, crashed through the rock with ease. Amazed the boy wanted to see if he had hurt himself. He certainly didn't feel any pain but wanted to make sure. Spying a puddle of water he looked down and gazed his beastly new reflection> A long horn rotruded from his forhead and his skin was a mottled grey. He was human up to his waist but had become a rhino above. He gasped and shot back, but for some reason this felt right. A gust of wind blew past him and he knew his conviction going forward. He was RHINOMAN and the plains were his to protect."
}

#2 - Print the entire dictionary

##print(story1)

#3 - Print the type of your dictionary
##print(type(story1))

#4 - Print only the keys
##print(story1.keys())

#5 - print only the values
##print(story1.values())

#6 - print the individual values using the keys (individually, lots of printi commands)
## print(story1["Start"])
## print(story1["Middle"])
## print(story1["End"])

#7 - Now let's add a new key:value pair.
    # 'hero': yourSuperHero
story1["Hero"] = "RHINOMAN"

#8 - All together
print(story1["Hero"])
print(story1["Start"])
print(story1["Middle"])
print(story1["End"])