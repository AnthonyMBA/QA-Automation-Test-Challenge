import allure

def before_scenario(context, scenario):
    allure.dynamic.title(scenario.name)

def after_step(context, step):
    if step.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(),
                      name="screenshot",
                      attachment_type=allure.attachment_type.PNG)
