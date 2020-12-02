# Backend Test Miio

## Installing the project

* First clone the project;
* Have the docker installed on your machine;
* In the folder where the project was cloned run the command docker-compose up --build;
* The django app is ready to be tested.

## Unitary tests

* With the project running perfectly it is possible to run the command "python manage.py test" to run a series of tests

## Endpoints and Json examples

* http://127.0.0.1:8000/owners/ Get and post are enabled to call or create an owner, Example of Json for creating onwer: {
   "name": "Owner test",
   "email": "test@test.com",
   "password": "test"
}

* http://127.0.0.1:8000/owners/owner_id/ This endpoint can be used to get, edit or delete a Owner;

* http://127.0.0.1:8000/regular-plans/ This endpoint can be used to get or create a RegularPlan, example of json for creation: {
   "name": "Regular Plan test",
   "tar_included": true,
   "subscription": 10.0,
   "cycle": "D",
   "type": "TS",
   "offer_iva": true,
   "off_peak_price": 10.0,
   "peak_price": 12.0,
   "unit": "KH",
   "valid": true,
   "publish": true,
   "vat": 1,
   "owner": null
}

* To get only RegularPlans with publish equal to true it is possible to pass a flag on the regular-plans/ endpoint, for example http://127.0.0.1:8000/regular-plans/?publish=true
* If you want to get only the RegularPlans from an owner, this is possible: http://127.0.0.1:8000/regular-plans/?name_owner=Owner Test
* http://127.0.0.1:8000/regular-plans/regualar_plan_id/ This endpoint can be used to get, edit or delete a RegularPlan;
