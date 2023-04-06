import os
import random

# specify path to local repository
repo_path = "https://github.com/n1cfury/commitment/blob/main"

# specify number of commits to generate
num_commits = random.randint(3, 19)

# generate and commit random changes
for i in range(num_commits):
    # generate random text file
    with open(os.path.join(repo_path, 'random.txt'), 'w') as f:
        f.write(str(random.randint(0, 1000000)))
    # stage and commit changes
    os.system('cd {0} && git add -A && git commit -m "Random commit #{1}"'.format(repo_path, i+1))
    
print('Generated {0} random commits.'.format(num_commits))
