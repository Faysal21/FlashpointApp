// For login and registration page ------------
async function login() {
  let usernameGiven = document.getElementById('uName').value;
  let passwordGiven = document.getElementById('pWord').value;

  let userCanLogin = false;

  const userListURL = 'http://localhost:7000/users';
  const userListResponse = await fetch(userListURL);
  const userList = await userListResponse.json();

  // Loop through the list and verify the right user
  for (let user in userList) {
    if (usernameGiven === userList[user].username && passwordGiven === userList[user].password) {
      userCanLogin = true;
      console.log("Welcome back, " + userList[user].username);
      sessionStorage.setItem("creds", userList[user].username);
      sessionStorage.setItem("role", userList[user].userRole);
      sessionStorage.setItem("userID", userList[user].userId);
      break;
    }
  }

  if (userCanLogin) {
    alert("Going to the home page...");
    // window.location.href="Home Page"
  }
  else alert("Credentials were invalid. Please try again.");
}

async function register() {
  let usernameGiven = document.getElementById('uName').value;
  let passwordGiven = document.getElementById('pWord').value;

  let userCanRegister = true;

  const userListURL = 'http://localhost:7000/users';
  const userListResponse = await fetch(userListURL);
  const userList = await userListResponse.json();

  for (let user of userList) {
    if (usernameGiven === user.username) userCanRegister = false;
  }

  if (!userCanRegister) alert("That username is taken. Please provide a different one.");
  // add the new user credentials to database
  else {
    const createUserData = {
      username: usernameGiven,
      password: passwordGiven,
      userRole: "Standard User"
    };
    const createUserOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(createUserData)
    };
    const createUserResponse = await fetch(userListURL, createUserOptions);
    const newUser = await createUserResponse.json();
    console.log(newUser);

    alert("Registration complete!");
    login();
  }
}

// For home page ------------------------------
function getMySets(userId) {

}

function getSets() {

}

// For card viewer page -----------------------
function getUserResponse() {

}

function revealAnswer() {

}

// For card/set creator/editor page -----------
function createNewDeck() {

}

function addNewCard(deck) {

}
