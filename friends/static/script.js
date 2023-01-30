function validateRegister() {

    var name = document.forms["registerForm"]["name"].value;
    var alias = document.forms["registerForm"]["alias"].value;
    var email = document.forms["registerForm"]["email"].value;
    var password = document.forms["registerForm"]["password"].value;
    var password_confirm = document.forms["registerForm"]["password-confirm"].value;
    var dob = document.forms["registerForm"]["dob"].value;

    if (name == "") {
        alert("Username must be filled out");
        return false;
    }
    if (email == "") {
        alert("Email must be filled out");
        return false;
    }
    if (password == "") {
        alert("Password must be filled out");
        return false;
    }
    if (password != password_confirm) {
        alert("Password and Confirm PW do not match");
        return false;
    }
    if (dob == "") {
        alert("Date of birth must be filled out");
        return false;
    }
    var dob_list = dob.split("-");
    var date = new Date(dob_list[0], dob_list[1], dob_list[2]);
    var today = new Date();
    var age = today.getFullYear() - date.getFullYear();
    if (age < 16) {
        alert("You must be 16 or older");
        return false;
    }

    const formData = new FormData();
    formData.append('name', name);
    formData.append('alias', alias);
    formData.append('email', email);
    formData.append('password', password);
    formData.append('birthday', dob);
    formData.append('csrfmiddlewaretoken', document.getElementsByName('csrfmiddlewaretoken')[0].value);


    fetch('./register', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Request failed');
        }).then(data => {
            window.location.href = `/friends?name=${name}`;
        })
        .catch(error => {

            console.log(error);
        });

    return true;
}

function validateLogin() {
    console.log(document.forms);
    var email = document.forms["loginForm"]["email-login"].value;
    var password = document.forms["loginForm"]["password-login"].value;
    if (email == "") {
        alert("Email must be filled out");
        return false;
    }
    if (password == "") {
        alert("Password must be filled out");
        return false;
    }

    const formData = new FormData();
    formData.append('email', email);
    formData.append('password', password);
    formData.append('csrfmiddlewaretoken', document.getElementsByName('csrfmiddlewaretoken')[0].value);

    fetch('./login', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Request failed');
        }).then(data => {
            var name = data['user_data']['name'];
            window.location.href = `/friends?name=${name}`;
        })
        .catch(error => {
            console.log(error);
            alert("wrong username or password");
        });

    return true;
}


function addFriend(user_id, f_id) {
    const formData = new FormData();
    formData.append('user_id', user_id);
    formData.append('new_friend', f_id);
    formData.append('csrfmiddlewaretoken', document.getElementsByName('csrfmiddlewaretoken')[0].value);

    fetch('./add_friend', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Request failed');
        }).then(data => {
            console.log(data);
            window.location.reload();
        })
        .catch(error => {
            console.log(error);
        });

    return true;
}

function removeFriend(user_id, f_id) {
    const formData = new FormData();
    formData.append('user_id', user_id);
    formData.append('to_delete', f_id);
    formData.append('csrfmiddlewaretoken', document.getElementsByName('csrfmiddlewaretoken')[0].value);

    fetch('./remove_friend', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
        .then(response => {
            if (response.ok) {
                return response.json();
            }
            throw new Error('Request failed');
        }).then(data => {
            console.log(data);
            window.location.reload();
        })
        .catch(error => {
            console.log(error);
        });

    return true;
}