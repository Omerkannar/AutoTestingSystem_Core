from flask import Flask, jsonify, render_template, send_from_directory, request
from flask_cors import CORS
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from apispec import APISpec
from datetime import datetime
import time
from Utils import Utils
from Utils import GlobalVariables

from marshmallow import Schema, fields

from Utils.Utils import replace_line
import threading

from werkzeug.utils import secure_filename

from AutoTest import AutoTest


# print("Main name: " + __name__)


class TestSchema(Schema):
    TestID = fields.Str()
    MainVersion = fields.Str()
    Name = fields.Str()
    Summary = fields.Str()
    ResultThreshold = fields.Str()
    RunTimeout = fields.Str()
    Prerequisite = fields.Str()
    Site = fields.Str()
    Environment = fields.Str()
    # StartPoint = fields.Str()


requested_command = r""


# test_list = []


# =======================================================================================================================
# Logger Last Commands
# =======================================================================================================================
def wait_to_logger_command(data, filename, write_mode):
    file = open(filename, write_mode)
    try:
        file.write(data)
    finally:
        file.close()


# =======================================================================================================================
# Global Data
# =======================================================================================================================
app = Flask(__name__, template_folder='./swagger/templates')
CORS(app)

spec = APISpec(
    title='flask-api-swagger-doc',
    version='1.0.0',
    openapi_version='3.0.2',
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)

auto_test = AutoTest()


# =======================================================================================================================
# Swagger Route Definition
# =======================================================================================================================
@app.route('/docs')
@app.route('/docs/<path:path>')
def swagger_docs(path=None):
    if not path or path == 'index.html':
        return render_template('index.html', base_url='/docs')
    else:
        return send_from_directory('./swagger/static', secure_filename(path))


@app.route('/api/swagger.json')
def create_swagger_spec():
    return jsonify(spec.to_dict())


# =======================================================================================================================
# Create Test
# =======================================================================================================================
@app.route("/create_test", methods=["POST"])
def create_test():
    """Post create_test_plan
          ---
          post:
            requestBody:
                required: true
                content:
                    application/json:
                        schema: TestSchema
          """
    print('start -> create_test')
    _timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if request.is_json:
        request_json = request.get_json()

        status, test_id = auto_test.do_create_test(request_json)

        # request_json = request.get_json()
        # print('type is ', type(request_json))
        #
        # print(request_json)
        print('finish -> create_test')
        # return request_json, 201
        return {"Status": status, "Id": test_id}, 201
    return {"Error": "Request must be JSON"}, 415


# =======================================================================================================================
# Get All Test
# =======================================================================================================================
@app.get("/get_all_test")
def get_all_test():
    """Get Test List
        ---
        get:
            description: get_test_plan_list
            responses:
                200:
                    description: Return Test List
                    content:
                        application/json:
                            schema: TestListSchema
        """
    test_list = Utils.return_Dictionary(GlobalVariables.parent_dir_test)
    print("Test_list is: ", test_list)
    return jsonify(test_list)


# =======================================================================================================================
# Prepare Test
# =======================================================================================================================
@app.route("/prepare_test", methods=["POST"])
def prepare_test():
    """Post prepare_test
          ---
          post:
            requestBody:
                required: true
                content:
                    application/json:
                        schema: TestIdSchema
          """
    print('start -> prepare_test')
    print(request)
    if request.is_json:
        request_json = request.get_json()
        test_id = request_json["data"][0]["test_id"] # For now, Take the first one
        test_name = request_json["data"][0]["test_name"]
        print('Prepare Test ID ->', test_id, ' Prepare Test Name ->', test_name)
        print(request_json)
        print('finish -> prepare_test')

        status = auto_test.do_prepare_test(test_id, test_name)

        return request_json, 201
    return {"Error": "Request must be JSON"}, 415


# =======================================================================================================================
# Main
# =======================================================================================================================
def flask_run():
    print("Running RestAPI")
    app.run(debug=True, use_reloader=False)


# def other_code(auto_test):
#     # Your other code here
#     print("Running AutoTestBE")
#     AutoTest.main(auto_test)


if __name__ == "__main__":
    # auto_test = AutoTest()

    flask_thread = threading.Thread(target=flask_run)
    # other_thread = threading.Thread(target=other_code(auto_test))

    flask_thread.start()

    # Allow some time for the Flask app to start before starting the other thread
    time.sleep(2)

    # other_thread.start()

    flask_thread.join()  # Wait for the Flask thread to finish (when you stop the server manually)
    # other_thread.join()  # Wait for the other thread to finish

    # auto_test = AutoTest()
    # requested_command = "Create1"
    # if requested_command == "Create":
    #     # auto_test.do_create_test()
    #     pass
