from flask import Flask, request, jsonify
import flask
import requests as rq
import json
import random
import time
import sys

app = Flask(__name__)

host = "http://hawking.sv.cmu.edu:8090"
# CMDA = "http://hawking.sv.cmu.edu:9005/serviceExecutionLog/addServiceExecutionLog"
CMDA = "http://localhost:9005/serviceExecutionLog/addServiceExecutionLog"
CMDATEST = "http://localhost:9075/serviceExecutionLog/addServiceExecutionLog"
CMDADEMO = "http://localhost:9098/serviceExecutionLog/addServiceExecutionLog"
remote = "http://cmda-test.jpl.nasa.gov:8080"

debug_mode = True

def serviceCall(parameters, message, staticPath, userId, frontend_url, backend_routing):
    print frontend_url

    # production mode
    if not debug_mode:
        remoteResp = rq.get(remote + backend_routing + "?" + parameters)
        resp = app.make_response(jsonify(remoteResp.json()))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    # debug mode
    dataUrl = host + "/static/" + staticPath + "/mock.nc"
    url = host + "/static/" + staticPath + "/mock.png"
    toCMDA = {"backend_url": host + backend_routing,
                "parameters": parameters + "&data_url=%s&image=%s" %(dataUrl, url),
                "userId": userId,
                "executionEndTime": int(time.time())*1000,
                "source": "mock",
                "executionStartTime": int(time.time())*1000,
                "frontend_url": frontend_url if frontend_url != None else ""}
    CMDAResp = rq.post(CMDA, json=toCMDA);
   # CMDARespTEST = rq.post(CMDATEST, json=toCMDA);
    CMDARespDEMO = rq.post(CMDADEMO, json=toCMDA);
    # print CMDAResp.content
    resp = app.make_response(jsonify({"dataUrl": dataUrl, "message": message, "success": True, "url": url}))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route("/debug")
def switchToDebug():
    global debug_mode
    debug_mode = True
    return "Switched to debug mode."

@app.route("/production")
def switchToProduction():
    global debug_mode
    debug_mode = False
    return "Switched to production mode."

@app.route("/svc/twoDimMap", methods=["GET"])
def twoDimMap():
    if request.method == "GET":
        return serviceCall(parameters = request.full_path.split("?")[1], 
                           message = "blablabla", 
                           staticPath = "universalPlotting", 
                           userId = int(request.args.get("userid")), 
                           frontend_url = request.args.get("fromPage"), 
                           backend_routing = "/svc/twoDimMap")
    else:
        return "Please use GET."

@app.route("/svc/EOF", methods=["GET"])
def EOF():
    if request.method == "GET":
        return serviceCall(parameters = request.full_path.split("?")[1], 
                           message = "blablabla", 
                           staticPath = "EOF", 
                           userId = int(request.args.get("userid")), 
                           frontend_url = request.args.get("fromPage"), 
                           backend_routing = "/svc/EOF")
    else:
        return "Please use GET."

@app.route("/svc/twoDimSlice3D", methods=["GET"])
def twoDimSlice3D():
    if request.method == "GET":
        return serviceCall(parameters = request.full_path.split("?")[1], 
                           message = "blablabla", 
                           staticPath = "twoDimSlice3D", 
                           userId = int(request.args.get("userid")), 
                           frontend_url = request.args.get("fromPage"), 
                           backend_routing = "/svc/twoDimSlice3D")
    else:
        return "Please use GET."

@app.route("/svc/scatterPlot2Vars", methods=["GET"])
def scatterPlot2Vars():
    if request.method == "GET":
        return serviceCall(parameters = request.full_path.split("?")[1], 
                           message = "blablabla", 
                           staticPath = "scatterPlot2Vars", 
                           userId = int(request.args.get("userid")), 
                           frontend_url = request.args.get("fromPage"), 
                           backend_routing = "/svc/scatterPlot2Vars")
    else:
        return "Please use GET."

@app.route("/svc/diffPlot2Vars", methods=["GET"])
def diffPlot2Vars():
    if request.method == "GET":
        return serviceCall(parameters = request.full_path.split("?")[1], 
                           message = "blablabla", 
                           staticPath = "diffPlot2Vars", 
                           userId = int(request.args.get("userid")), 
                           frontend_url = request.args.get("fromPage"), 
                           backend_routing = "/svc/diffPlot2Vars")
    else:
        return "Please use GET."

@app.route("/svc/correlationMap", methods=["GET"])
def correlationMap():
    if request.method == "GET":
        return serviceCall(parameters = request.full_path.split("?")[1], 
                           message = "blablabla", 
                           staticPath = "correlationMap", 
                           userId = int(request.args.get("userid")), 
                           frontend_url = request.args.get("fromPage"), 
                           backend_routing = "/svc/correlationMap")
    else:
        return "Please use GET."

@app.route("/svc/randomForest", methods=["GET"])
def randomForest():
    if request.method == "GET":
        return serviceCall(parameters = request.full_path.split("?")[1], 
                           message = "blablabla", 
                           staticPath = "randomForest", 
                           userId = int(request.args.get("userid")), 
                           frontend_url = request.args.get("fromPage"), 
                           backend_routing = "/svc/randomForest")
    else:
        return "Please use GET."

@app.route("/svc/conditionalPdf", methods=["GET"]) # no plots and data
def conditionalPdf():
    if request.method == "GET":
        return serviceCall(parameters = request.full_path.split("?")[1], 
                           message = "blablabla", 
                           staticPath = "conditionalPdf", 
                           userId = int(request.args.get("userid")), 
                           frontend_url = request.args.get("fromPage"), 
                           backend_routing = "/svc/conditionalPdf")
    else:
        return "Please use GET."

@app.route("/svc/anomaly", methods=["GET"])
def anomaly():
    if request.method == "GET":
        return serviceCall(parameters = request.full_path.split("?")[1], 
                           message = "blablabla", 
                           staticPath = "anomaly", 
                           userId = int(request.args.get("userid")), 
                           frontend_url = request.args.get("fromPage"), 
                           backend_routing = "/svc/anomaly")
    else:
        return "Please use GET."

@app.route("/svc/timeSeries", methods=["GET"])
def timeSeries():
    if request.method == "GET":
        return serviceCall(parameters = request.full_path.split("?")[1], 
                           message = "blablabla", 
                           staticPath = "timeSeries", 
                           userId = int(request.args.get("userid")), 
                           frontend_url = request.args.get("fromPage"), 
                           backend_routing = "/svc/timeSeries")
    else:
        return "Please use GET."

@app.route("/svc/twoDimZonalMean", methods=["GET"])
def twoDimZonalMean():
    if request.method == "GET":
        return serviceCall(parameters = request.full_path.split("?")[1], 
                           message = "blablabla", 
                           staticPath = "twoDimZonalMean", 
                           userId = int(request.args.get("userid")), 
                           frontend_url = request.args.get("fromPage"), 
                           backend_routing = "/svc/twoDimZonalMean")
    else:
        return "Please use GET."

@app.route("/svc/threeDimZonalMean", methods=["GET"])
def threeDimZonalMean():
    if request.method == "GET":
        return serviceCall(parameters = request.full_path.split("?")[1], 
                           message = "blablabla", 
                           staticPath = "threeDimZonalMean", 
                           userId = int(request.args.get("userid")), 
                           frontend_url = request.args.get("fromPage"), 
                           backend_routing = "/svc/threeDimZonalMean")
    else:
        return "Please use GET."

@app.route("/svc/threeDimVarVertical", methods=["GET"])
def threeDimVarVertical():
    if request.method == "GET":
        return serviceCall(parameters = request.full_path.split("?")[1], 
                           message = "blablabla", 
                           staticPath = "threeDimVarVertical", 
                           userId = int(request.args.get("userid")), 
                           frontend_url = request.args.get("fromPage"), 
                           backend_routing = "/svc/threeDimVarVertical")
    else:
        return "Please use GET."

@app.route("/svc/mapView", methods=["GET"])
def mapView():
    if request.method == "GET":
        return serviceCall(parameters = request.full_path.split("?")[1], 
                           message = "blablabla", 
                           staticPath = "mapView", 
                           userId = int(request.args.get("userid")), 
                           frontend_url = request.args.get("fromPage"), 
                           backend_routing = "/svc/mapView")
    else:
        return "Please use GET."

@app.route("/svc/conditionalSampling2Var", methods=["GET"])
def conditionalSampling2Var():
    if request.method == "GET":
        return serviceCall(parameters = request.full_path.split("?")[1], 
                           message = "blablabla", 
                           staticPath = "conditionalSampling2Var", 
                           userId = int(request.args.get("userid")), 
                           frontend_url = request.args.get("fromPage"), 
                           backend_routing = "/svc/conditionalSampling2Var")
    else:
        return "Please use GET."

@app.route("/svc/regridAndDownload", methods=["GET"])  # no plots and data
def regridAndDownload():
    if request.method == "GET":
        return serviceCall(parameters = request.full_path.split("?")[1], 
                           message = "blablabla", 
                           staticPath = "regridAndDownload", 
                           userId = int(request.args.get("userid")), 
                           frontend_url = request.args.get("fromPage"), 
                           backend_routing = "/svc/regridAndDownload")
    else:
        return "Please use GET."

@app.route("/svc/conditionalSampling", methods=["GET"])
def conditionalSampling():
    if request.method == "GET":
        return serviceCall(parameters = request.full_path.split("?")[1], 
                           message = "blablabla", 
                           staticPath = "conditionalSampling", 
                           userId = int(request.args.get("userid")), 
                           frontend_url = request.args.get("fromPage"), 
                           backend_routing = "/svc/conditionalSampling")
    else:
        return "Please use GET."

@app.route("/svc/timeSeriesWorkFlow", methods=["GET"]) # no plots and data
def timeSeriesWorkFlow():
    if request.method == "GET":
        return serviceCall(parameters = request.full_path.split("?")[1], 
                           message = "blablabla", 
                           staticPath = "timeSeriesWorkFlow", 
                           userId = int(request.args.get("userid")), 
                           frontend_url = request.args.get("fromPage"), 
                           backend_routing = "/svc/timeSeriesWorkFlow")
    else:
        return "Please use GET."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "debug":
            debug_mode = True
        else:
            debug_mode = False
    app.run(port=8090, host= '0.0.0.0')
