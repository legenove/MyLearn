/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var ToplineId = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            content   'ref' 
            is_public   'boolean' 
            is_top   'boolean' 
            order_score   'integer' 
            short_title   'string' 
            
        @success
            status 200    type:object
            operator_id   'ref' 
            date_updated   'ref' 
            order_score   'integer' 
            question   'ref' 
            short_title   'string' 
            is_top   'boolean' 
            is_public   'boolean' 
            date_created   'ref' 
            id   'integer' 
            question_id   'ref' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/topline/" + obj.id + "",
            method: "PUT",
            data: {
                content: obj.content,
                is_public: obj.is_public,
                is_top: obj.is_top,
                order_score: obj.order_score,
                short_title: obj.short_title
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
    
    /*
        @params obj 'data params'
            id   'string' string id in path
            
        @success
            status 204    type:object
            ok   'boolean' 
            
    */
    this.delete = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/topline/" + obj.id + "",
            method: "DELETE",
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
    ToplineId: new ToplineId
};