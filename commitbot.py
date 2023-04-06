import os
import random
import urllib.request

# specify URL of raw text file in repository
url = "https://raw.githubusercontent.com/n1cfury/commitment/main/random.txt"

# specify number of commits to generate
num_commits = random.randint(3, 19)

# generate and commit random changes
for i in range(num_commits):
    # generate random text file
    with urllib.request.urlopen(url) as response, open('random.txt', 'wb') as f:
        f.write(response.read())
    # stage and commit changes
    os.system('git add -A && git commit -m "Random commit #{0}"'.format(i+1))
    
print('Generated {0} random commits.'.format(num_commits))
