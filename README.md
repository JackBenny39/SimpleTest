# Eclipse and GitHub

## Part 1: From GitHub to Eclipse

### Step1: Create a simple public project on GitHub (this project) with two branches: master and brancher

![GitHub Project](/images/github1.png)

Note: This is for exposition. You don't have to do this! We will work with this repository (repo, from now on) for the Eclipse demonstration.

### Step 2: Add repository from GitHub to local Git
1. Window > Show View > Other

![Eclipse Show View](/images/eclipse1.png)

2. > Git > Git Repositories

![Eclipse Repo View](/images/eclipse2.png)

3. Click button: Clone a Git Repository and add the clone to this view

![Eclipse Repo Clone Button](/images/eclipse3.png)

4. Copy/Paste GitHub repo URI to Window Directory

![GitHub URI](/images/github2.png)

![Eclipse Add Directory](/images/eclipse4.png)

5. Next, choose branches: typically master and the branch you want.

![Eclipse Choose Branches](/images/eclipse5.png)

![Eclipse Local Repo Location](/images/eclipse6.png)

SimpleTest is now one of the Git Repositories!

![Eclipse Local Repo Location](/images/eclipse7.png)

### Step 3: Add project to Eclipse Workspace
1. File > New > PyDev Project

![Eclipse PyDev Project](/images/eclipse8.png)

Note: Uncheck the default to then choose your own Git repo address (the one you just created above). Typically do not want the workspace and the Git version control directory to be the same. Give the project a name.

![Eclipse Local Repo Choice](/images/eclipse9.png)

2. Click Browse, then navigate to and choose the local Git repo

![Eclipse Local Repo Location](/images/eclipse10.png)

SimpleTest is now in the Eclipse PyDev Package Explorer

![Eclipse PyDev Package](/images/eclipse11.png)

### Step 4: Load the working branch, brancher
All Git commands are via the Team dropdown menu choice. 

1. Right click on the SimpleTest Package then Team > Switch To > Other

![Eclipse Switch Branch](/images/eclipse12.png)

2. Highlight (click on) the desirted branch (brancher), then click Checkout

![Eclipse Checkout Branch](/images/eclipse13.png)








