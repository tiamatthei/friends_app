function validateRegister() {
    var name = document.forms["registerForm"]["name"].value;
    var alias = document.forms["registerForm"]["alias"].value;
    var email = document.forms["registerForm"]["email"].value;
    var password = document.forms["registerForm"]["password"].value;
    var dob = document.forms["registerForm"]["dob"].value;
    console.log(document.getElementsByName('csrfmiddlewaretoken')[0].value);

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
    if (dob == "") {
        alert("Date of birth must be filled out");
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
                return response;
            }
            throw new Error('Request failed');
        }).then(data => {
            fetch('./friends', {
                method: 'GET',
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                }
            })

        })
        .catch(error => {

            console.log(error);
        });

    return true;
}

function validateLogin() {
    var username = document.forms["registerForm"]["username"].value;
    var email = document.forms["registerForm"]["email"].value;
    var password = document.forms["registerForm"]["password"].value;
    var dob = document.forms["registerForm"]["dob"].value;

    if (username == "") {
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
    if (dob == "") {
        alert("Date of birth must be filled out");
        return false;
    }
    return true;
}