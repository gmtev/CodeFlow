## :warning: Важно за проверяващите!/Important for reviewers! :warning:
Deployed at https://codeflow-chfchee9gkeuf6c3.italynorth-01.azurewebsites.net/ 

Тази репозитория е оставена за localhost версия на проекта; репозиторията на deploy-натата версия е https://github.com/gmtev/CodeFlowDeployed 

Единствената разлика е в настройките на проекта, но това repo е посочено като официалното за нагледност и поради неизбежното изтичане на безплатния лимит.

This repository is left for the localhost version of the project; the deployed one is https://github.com/gmtev/CodeFlowDeployed 

The only difference is in the project settings, but this repo has been designated as the official one for reference and due to the inevitable exhaustion of the free limit.

В/към анкетата за моя проект има прикачен Google Docs файл, където са налични всички нужни данни за стартирането на проекта. Той ще бъде обновяван при всяко нужно ново вписване. Отделно в долната част на "README" ще бъде показана нужната информация. При наличие на проблеми, липса на данни в документа или несъответствие, можете да се свържете с мен по всяко време. Под описанието на проекта са прикачени и релевантни снимки с цел нагледност. Благодаря Ви предварително! :relaxed:

Attached to the survey form for my project is a Google Docs file that contains all the necessary data for starting the project. This document will be updated with every required new entry. Additionally, the necessary information will be displayed at the bottom of the "README" file. If you encounter any issues, missing data in the document, or discrepancies, you can contact me at any time. The description of the project is accompanied by relevant images for visual representation. Thank you in advance! :relaxed:

# SoftUni Django Advanced Course Project - CodeFlow :computer: 

In this repository, I will upload my project for **SoftUni's Django Advanced course**. It is made in accordance with the requirements of the task; all static images are royalty-free/stock images.
Project description:
- A platform for users to publish questions/lectures regarding coding and to interact with one another.
- Implemented using the Django Framework.
- Has 24 CBV's, 5 independent models, 17 forms (most of them inherit a base class), 21 templates and two custom error pages (404 and 403) extending a base.html file, a navbar and a greeting/goodbye email html files.
- Used Django Template Engine and a bit of JS at certain places; Bootstrap was used for the design. 
- Uses PostgreSQL as a database service.
- Register/Login/Logout functionality with a public and a private part. Users have CRUD permissions for their related content/profile, unregistered users can only access the home page (and even if they can reach the questions or lectures dashboard by url, every next option would redirect them again to the login page). Trying to guess the needed url to access other user's edit/delete profile/credentials/content results in being redirected to the custom 403 page.
- Customized admin site with 5 custom options to each interface; two groups of admins - superusers with full CRUD permissions and staff with CRUD permissions regarding the content (questions/lectures/sections). Roles can be managed/assigned from the site.
- Exception handling and data validations.
- Extended the Django user (login with either username or email) and had him in a one-to-one with the Profile model.
- RESTful Likes and Comments (like/unlike, add and remove comment).
- Likes and Comments implemented with generic foreign key in order to be more flexible for future development or changes in the project structure, as well as them being easy to be "taken out" of the project and be used elsewhere, otherwise they would be tied to the common parent model of Question and Lecture.
- Cloudinary used for image uploads (5 mb validation limit).
- Integrated Markdown for the Question/Lecture/Section textfield.
- Sending a greeting upon registration and a goodbye email upon profile deletion using MAILJET.
- 13 tests written (remove the signals for profile creation which send greeting emails to new users while testing).
  
## Required External APIs and Secret Keys :key:

The following external API keys and secret keys are required to run the localhost version of the project:
- **SECRET_KEY**: unavailable in GitHub for safety reasons.
- **MAILJET_API_KEY**: Mailjet API Key. 
- **MAILJET_SECRET_KEY**: Mailjet Secret Key.  
- **cloudinary_cloud_name/cloud_name**: Your Cloudinary Cloud Name.
- **MEDIA_URL = "https://res.cloudinary.com/cloud_name_goes_here/" must contain the aforementioned cloud_name!** 
- **В MEDIA_URL = "https://res.cloudinary.com/cloud_name_goes_here/" трябва да бъде поставена гореспоменатата cloud_name променлива.**
- **cloudinary_api_key**: Cloudinary API Key.  
- **cloudinary_api_secret**: Cloudinary API Secret Key.
- Database credentials in settings.py

  ## Screenshots - below I will upload screenshots of the project as it is being developed. :framed_picture:
![1](https://github.com/user-attachments/assets/5e9cc9b6-1bef-4255-a41d-c7b7b66320e9)
![2](https://github.com/user-attachments/assets/aa7dcfb3-d12d-4fa8-90c2-901c7e09c0df)
![3](https://github.com/user-attachments/assets/459a3315-af43-4cae-b245-c0e2f738c39b)
![4](https://github.com/user-attachments/assets/e754b648-8257-482b-8170-732659bd2500)
![5](https://github.com/user-attachments/assets/11800ef3-11a0-4f90-b65d-716520121258)
![6](https://github.com/user-attachments/assets/4fe95ff0-33a9-48c2-88fa-5d8b909efb14)
![7](https://github.com/user-attachments/assets/9bc489a5-177e-4741-bcc1-a6590999ce45)
![8](https://github.com/user-attachments/assets/d5541d84-3be7-4f14-ab6d-e3f4c9b3d4b3)
![9](https://github.com/user-attachments/assets/608bf12e-b86b-43cf-ae20-64cd21109ebc)
![10](https://github.com/user-attachments/assets/ee9b78a2-e71d-4c2e-a839-355e6887b0f0)
![11](https://github.com/user-attachments/assets/8b674dbc-7123-4172-9d2a-17395497a75c)
![12](https://github.com/user-attachments/assets/92b50e1c-aff7-4f19-97ce-607ff7112922)
![121](https://github.com/user-attachments/assets/f4c21c6d-f8e4-4485-8966-093c94b74306)
![13](https://github.com/user-attachments/assets/5c779175-4cae-4e30-8cf0-a09cb77405f7)
![14](https://github.com/user-attachments/assets/3e3865c4-d564-473c-8b93-aa5c9518bf2a)
![15](https://github.com/user-attachments/assets/4de27b0e-f205-47e5-9763-7c031ccc339a)
![16](https://github.com/user-attachments/assets/5ce30a38-18cc-43d8-b605-4cab61861c19)
![17](https://github.com/user-attachments/assets/a085694c-8d53-47b9-9b8e-c2e1ed08b6c9)
![18](https://github.com/user-attachments/assets/8730eb32-1d52-4305-a1de-1f4007a98b5d)
![19](https://github.com/user-attachments/assets/50ce5b4f-f001-446f-a50e-b3efd3b3d120)
![20](https://github.com/user-attachments/assets/df6594ee-5f6f-4f9b-bba3-445116409c3a)
![21](https://github.com/user-attachments/assets/573923ba-a954-4026-bb0c-2e8d90cc3387)
![mail1](https://github.com/user-attachments/assets/d1775773-175c-4713-9edb-3d6a3553531c)
![mail2](https://github.com/user-attachments/assets/0380390c-e746-4c41-b51e-58d6ed888268)
![ednoto](https://github.com/user-attachments/assets/423b316d-ab26-46e2-b10b-32eb23313823)
![slednego](https://github.com/user-attachments/assets/9446ae69-30e6-4990-a9d9-ccce7ff61a8f)
![comment3](https://github.com/user-attachments/assets/b66e320c-e8b4-4f46-8643-4cc3b3f8e879)
![comment4api](https://github.com/user-attachments/assets/0c4aa90b-71fa-4609-a9c7-e65d691f7d6d)
![stana tuka](https://github.com/user-attachments/assets/c1a5b949-76fe-405c-be56-a3e855f1b0f4)
![i tam](https://github.com/user-attachments/assets/7f7921ce-0153-4b56-a0e8-0bd1a1c16b86)
![403](https://github.com/user-attachments/assets/5802059f-7939-46e8-9eda-d9ae2248a09d)
![404](https://github.com/user-attachments/assets/10e2659c-9f71-4dd2-8298-e62d7477c58d)
![edituser](https://github.com/user-attachments/assets/14fa0018-d6f4-4d5c-afcd-cf0d62fc4b1a)
![tests](https://github.com/user-attachments/assets/99233d94-cc66-46f2-b69e-820fb94545b9)






















