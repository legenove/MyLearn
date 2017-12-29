/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Qualification = function () {
    /*
        @params obj 'data params'
            
        @success
            status 200    type:object
            status   'ref' 
            account_id   'ref' 
            title   'string' 
            reasons   'string' 
            explain   'string' 
            tag_id   'ref' 
            name   'string' 
            tag_name   'string' 
            images   'array' 
            type   'ref' 
            id   'ref' 
            additional   'string' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/qualification",
            method: "GET",
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
            name   'string' 
            explain   'string' 
            tag_id   'integer' 
            images   'array' 
            type   'ref' 
            additional   'string' 
            
        @success
            status 201    type:object
            status   'ref' 
            account_id   'ref' 
            title   'string' 
            reasons   'string' 
            explain   'string' 
            tag_id   'ref' 
            name   'string' 
            tag_name   'string' 
            images   'array' 
            type   'ref' 
            id   'ref' 
            additional   'string' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/qualification",
            method: "POST",
            data: {
                name: obj.name,
                explain: obj.explain,
                tag_id: obj.tag_id,
                images: obj.images,
                type: obj.type,
                additional: obj.additional
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
    Qualification: new Qualification
};