// App JS

document.addEventListener('DOMContentLoaded', () => {
    const newDriverForm = document.querySelector('#new-driver-form');
    newDriverForm.addEventListener('submit', handleNewDriverFormSubmit);

    const deleteAllButton = document.querySelector('#delete-drivers');
    deleteAllButton.addEventListener('click', handleDeleteAllClick);
})

const handleNewDriverFormSubmit = function (event) {
    event.preventDefault();

    const driverListItem = createDriverListItem(event.target);
    const driverList = document.querySelector('#driver-list');
    driverList.appendChild(driverListItem);

    event.target.reset();
}

const createDriverListItem = function (form) {
    const driverListItem = document.createElement('li');
    driverListItem.classList.add('driver-list-item')

    const driver = document.createElement('h2');
    driver.textContent = form.driver.value;
    driverListItem.appendChild(driver);

    const team = document.createElement('h3');
    team.textContent = form.team.value;
    driverListItem.appendChild(team);

    const nationality = document.createElement('h3');
    nationality.textContent = form = form.nationality.value;
    driverListItem.appendChild(nationality);

    return driverListItem;
}

const handleDeleteAllClick = function (event) {
    const driverList = document.querySelector('#driver-list');
    driverList.innerHTML = '';
}