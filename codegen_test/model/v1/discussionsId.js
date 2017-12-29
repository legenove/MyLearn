/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var DiscussionsId = function () {
    /*
        @params obj 'data params'
            id   'string' question discussion id in path
            duration   'integer' 
            content   'string' 
            media_id   'ref' 
            qiniu_id   'string' 
            source   'string' 
            
        @success
            status 201    type:object
            status   'string' 
            account_id   'integer' 
            account_role   'string' 
            content   'string' 
            type   'string' 
            id   'ref' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/discussions/" + obj.id + "",
            method: "POST",
            data: {
                duration: obj.duration,
                content: obj.content,
                media_id: obj.media_id,
                qiniu_id: obj.qiniu_id,
                source: obj.source || "weixin"
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
    DiscussionsId: new DiscussionsId
};