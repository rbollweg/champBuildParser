__author__ = 'The Gibs'

#!flask/bin/python
from app import app
from app import db, models
import datetime
if __name__ == "__main__":
    #---------Delete Everything in DB--------
    #matches = models.Match.query.all()
    #for match in matches:
    #    db.session.delete(match)
    #
    #builds = models.Build.query.all()
    #for build in builds:
    #    db.session.delete(build)
    #
    #steps = models.Step.query.all()
    #for step in steps:
    #    db.session.delete(step)

    #items = models.Step.query.all()
    #for item in items:
    #    db.session.delete(item)
    #---------------------------------------
    #-----------Add some mocked build-------
    # match = models.Match(url="http://matchhistory.na.leagueoflegends.com/en/#match-details/TRLH1/30054?gameHash=055b17da8456fdc8&tab=builds", date_play = datetime.datetime.now())
    # build = models.Build(champ_name = "Gnar", match = match)
    # step_repo = []
    # step1 = models.Step(time = "0:07", build = build)
    # step_repo.append(step1)
    # step2 = models.Step(time = "5:52", build = build)
    # step_repo.append(step2)
    # step3 = models.Step(time = "7:03", build = build)
    # step_repo.append(step3)
    # step4 = models.Step(time = "12:13", build = build)
    # step_repo.append(step4)
    # step5 = models.Step(time = "13:03", build = build)
    # step_repo.append(step5)
    # step6 = models.Step(time = "15:52", build = build)
    # step_repo.append(step6)
    # step7 = models.Step(time = "17:52", build = build)
    # step_repo.append(step7)
    # step8 = models.Step(time = "20:23", build = build)
    # step_repo.append(step8)
    #
    # item_repo = []
    # item1step1 = models.Item(item = "Dorans Blade", step=step1)
    # item_repo.append(item1step1)
    # item2step1 = models.Item(item = "Health Potion", step=step1)
    # item_repo.append(item2step1)
    # item3step1 = models.Item(item = "Warding Totem", step=step1)
    # item_repo.append(item3step1)
    #
    # item1step2 = models.Item(item = "Giant's Belt", step=step2)
    # item_repo.append(item1step2)
    # item2step2 = models.Item(item = "Sight Ward", step=step2)
    # item_repo.append(item2step2)
    # item3step2 = models.Item(item = "Health Potion", step=step2)
    # item_repo.append(item3step2)
    #
    # item1step3 = models.Item(item = "Health Potion", step=step3)
    # item_repo.append(item1step3)
    # item2step3 = models.Item(item = "Sweeper", step=step3)
    # item_repo.append(item2step3)
    #
    # item1step4 = models.Item(item = "Sunfire Cape", step=step4)
    # item_repo.append(item1step4)
    #
    # item1step5 = models.Item(item = "Giant's Belt", step=step5)
    # item_repo.append(item1step5)
    #
    # item1step6 = models.Item(item = "Health Potion", step=step6)
    # item_repo.append(item1step6)
    # item2step6 = models.Item(item = "Vision Ward", step=step6)
    # item_repo.append(item2step6)
    # item3step6 = models.Item(item = "Warden's Mail", step=step6)
    # item_repo.append(item3step6)
    #
    # item1step7 = models.Item(item = "Boots of Speed", step=step7)
    # item_repo.append(item1step7)
    # item2step7 = models.Item(item = "Health Potion", step=step7)
    # item_repo.append(item2step7)
    #
    # item1step8 = models.Item(item = "Sight Ward", step=step8)
    # item_repo.append(item1step8)
    #
    # db.session.add(match)
    # db.session.add(build)
    # for step in step_repo:
    #     db.session.add(step)
    # for item in item_repo:
    #     db.session.add(item)
    #db.session.commit()
    #--------------------------------------
    #-------Run app------------------------
    app.run(debug=True)