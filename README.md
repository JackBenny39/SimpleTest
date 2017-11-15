# Eclipse and GitHub

## Part 1: From GitHub to Eclipse

### Step 1: Create a simple public project on GitHub (this project) with two branches: master and brancher

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

![Eclipse Switch Branch 1](/images/eclipse12.png)

2. Highlight (click on) the desired branch (brancher), then click Checkout

![Eclipse Checkout Branch 1](/images/eclipse13.png)

3. Checkout as New Local Branch

![Eclipse Checkout Branch 2](/images/eclipse14.png)

3. Create Local Branch

![Eclipse Checkout Branch 3](/images/eclipse15.png)

3. Eclipse Switched to brancher branch

![Eclipse Switch Branch 2](/images/eclipse16.png)



## Part 2: Working on another's Project

### Step 1: Create an Issue in GitHub

1. Go to GitHub > Issues 

2. Type in Title and Comments
![GitHub Issue 1](/images/github_issue1a.png)
Submit!

3. Owner comments and requests that you clone the repo (see part 1, above), create a local branch, mess around, Push and Commit when necessary. Note: Push from Eclipse merely establishes the reference, you still have to Commit changes if you want to maintain version control in the remote.
![GitHub Issue 2](/images/github_issue2.png)


### Step 2: Mess about in Eclipse

1. After cloning, create a new Branch in local
![Eclipse Issue 1](/images/eclipse_issue1.png)

2. Be sure the source is master (or whatever branch you want to clone from) and give the new branch a name
![Eclipse Issue 2](/images/eclipse_issue2.png)

3. Make updates
![Eclipse Issue 3](/images/eclipse_issue3.png)

4. Write a test
![Eclipse Issue 4](/images/eclipse_issue4.png)

5. Run the test - Use the green Start Button and choose Run As > Python unit-test
![Eclipse Issue 5](/images/eclipse_issue5.png)

6. It passed!
![Eclipse Issue 6](/images/eclipse_issue6.png)

7. You can Push your new branch to establish it in GitHub
![Eclipse Issue 7](/images/eclipse_issue7.png)

![Eclipse Issue 8](/images/eclipse_issue8.png)

8. Commit code changes when you are ready
![Eclipse Issue 9](/images/eclipse_issue9.png)

Note: the staged changes in the Git Staging menu
![Eclipse Issue 10](/images/eclipse_issue10.png)

After hitting Commit and Push and entering credentials...
![Eclipse Issue 11](/images/eclipse_issue11.png)
The little yellow bars next to the files indicate that your local and remote files are identical.

And, your commit is now reflected in GitHub
![GitHub Issue 3](/images/github_issue3.png)

### Step 3: Pull Request in Github

1. Pull Request
![GitHub Issue 4](/images/github_issue4.png)

2. Type in Title and comment. Note: I forgot to reference the Issue - but this would be the place to do it!
![GitHub Issue 5](/images/github_issue5.png)

3. Owner Merges the PR - could solicit comments from others here, as well
![GitHub Issue 6](/images/github_issue6.png)
And, confirms
![GitHub Issue 7](/images/github_issue7.png)

4. Owner deletes branch on remote
![GitHub Issue 9](/images/github_issue9.png)
Success...
![GitHub Issue 10](/images/github_issue10.png)
Branch no longer available in GitHub
![GitHub Issue 11](/images/github_issue11.png)

### Step 4: Update local in Eclipse to reflect changes in master and branch in remote GitHub

1. summer branch is still available in Eclipse - switch to master
![Eclipse Issue 12](/images/eclipse_issue12.png)

And, in master, the code does not reflect the changes in the summer branch

![Eclipse Issue 13](/images/eclipse_issue13.png)

2. Pull master from remote GitHub - be sure to be in master in Eclipse
![Eclipse Issue 14](/images/eclipse_issue14.png)
![Eclipse Issue 15](/images/eclipse_issue15.png)

Hit Okay
![Eclipse Issue 16](/images/eclipse_issue16.png)

master now reflects updated code
![Eclipse Issue 17](/images/eclipse_issue17.png)

3. Delete summer branch from local
![Eclipse Issue 18](/images/eclipse_issue18.png)


