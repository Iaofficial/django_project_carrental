document.addEventListener("DOMContentLoaded", function () {

    // Mobile navigation menu

    const menuButton = document.querySelector(".menu-toggle");
    const navigation = document.querySelector("#siteNav");

    if (menuButton && navigation) {

        menuButton.addEventListener("click", function () {

            const isOpen = navigation.classList.toggle("open");

            menuButton.setAttribute(
                "aria-expanded",
                String(isOpen)
            );

            menuButton.textContent = isOpen ? "✕" : "☰";

        });

    }


    // Scroll reveal animation

    const revealElements = document.querySelectorAll(".reveal");

    if ("IntersectionObserver" in window) {

        const observer = new IntersectionObserver(
            function (entries, currentObserver) {

                entries.forEach(function (entry) {

                    if (entry.isIntersecting) {

                        entry.target.classList.add("is-visible");

                        currentObserver.unobserve(entry.target);

                    }

                });

            },
            {
                threshold: 0.12
            }
        );

        revealElements.forEach(function (element) {
            observer.observe(element);
        });

    } else {

        revealElements.forEach(function (element) {
            element.classList.add("is-visible");
        });

    }


    // Search available cars

    const searchInput = document.querySelector("#carSearch");

    const carCards = document.querySelectorAll(".searchable-car");

    const noCarsMessage = document.querySelector("#noCarsMessage");

    if (searchInput) {

        searchInput.addEventListener("input", function () {

            const searchValue = searchInput.value.toLowerCase();

            let visibleCount = 0;

            carCards.forEach(function (card) {

                const carName = card.textContent.toLowerCase();

                const matches = carName.includes(searchValue);

                card.style.display = matches ? "" : "none";

                if (matches) {
                    visibleCount++;
                }

            });

            if (noCarsMessage) {
                noCarsMessage.hidden = visibleCount !== 0;
            }

        });

    }


    // Booking date validation

    const pickupDate = document.querySelector("#pickup_date");

    const returnDate = document.querySelector("#return_date");

    const dateHint = document.querySelector("#dateHint");

    const bookingForm = document.querySelector("#bookingForm");


    function updateReturnDate() {

        if (!pickupDate || !returnDate) {
            return;
        }

        if (pickupDate.value) {

            const minimumDate = new Date(
                pickupDate.value + "T00:00:00"
            );

            minimumDate.setDate(minimumDate.getDate() + 1);

            const year = minimumDate.getFullYear();

            const month = String(
                minimumDate.getMonth() + 1
            ).padStart(2, "0");

            const day = String(
                minimumDate.getDate()
            ).padStart(2, "0");

            returnDate.min = `${year}-${month}-${day}`;

            if (
                returnDate.value &&
                returnDate.value <= pickupDate.value
            ) {
                returnDate.value = "";
            }

            if (dateHint) {
                dateHint.textContent =
                    "Return date must be after pickup date.";
            }

        }

    }


    if (pickupDate && returnDate) {

        // Prevent selecting past pickup dates.

        const today = new Date();

        const todayString =
            today.getFullYear() + "-" +
            String(today.getMonth() + 1).padStart(2, "0") + "-" +
            String(today.getDate()).padStart(2, "0");

        pickupDate.min = todayString;

        returnDate.min = todayString;

        pickupDate.addEventListener("change", updateReturnDate);

        if (bookingForm) {

            bookingForm.addEventListener("submit", function (event) {

                if (
                    !pickupDate.value ||
                    !returnDate.value ||
                    returnDate.value <= pickupDate.value
                ) {

                    event.preventDefault();

                    if (dateHint) {
                        dateHint.textContent =
                            "Please select a valid return date.";
                    }

                }

            });

        }

    }

});