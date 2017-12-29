/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AppQuestionsId = function () {
    /*
        @params obj 'data params'
            id   'string' question id in path
            duration   'integer' 
            source   'string' 
            media_id   'ref' 
            qiniu_id   'string' 
            
        @success
            status 201    type:object
            likings_count   'integer' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/app/questions/" + obj.id + "",
            method: "POST",
            data: {
                duration: obj.duration,
                source: obj.source || "weixin",
                media_id: obj.media_id,
                qiniu_id: obj.qiniu_id
                },
            success: function (res) {
                typeof obj.success === 'function' && obj.success(res);
            },
            fail: function (res) {
                typeof obj.fail === 'function' && obj.fail(res);
            },
            complete: function (res) {
                typeof obj.complete === 'function' && obj.complete(res);
            }
        })
    };
    

};

module.exports = {
    AppQuestionsId: new AppQuestionsId
};