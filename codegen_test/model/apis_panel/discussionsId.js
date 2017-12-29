/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var DiscussionsId = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            status   'string' 
            is_hidden   'boolean' 
            
        @success
            status 200    type:object
            status   'string' 
            account_id   'integer' 
            date_updated   'ref' 
            account_role   'string' 
            order_score   'integer' 
            content   'string' 
            date_created   'ref' 
            is_hidden   'boolean' 
            type   'string' 
            id   'ref' 
            question_id   'ref' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/discussions/" + obj.id + "",
            method: "PUT",
            data: {
                status: obj.status,
                is_hidden: obj.is_hidden
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