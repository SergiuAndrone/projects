//
//  AppDelegate.m
//  The Detonator
//
//  Created by sergiuandrone on 28/11/2019.
//  Copyright © 2019 sergiuandrone. All rights reserved.
//

#import "AppDelegate.h"
#import "Samples.h"

@interface AppDelegate ()

@property (weak) IBOutlet NSWindow *window;
@end

@implementation AppDelegate

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification {
    // Insert code here to initialize your application
    [Samples createDefaulLocation];
    int _totalCount = 0;
    _samplesDropped.stringValue = [NSString stringWithFormat:@"%d", _totalCount];
    _progressBar.indeterminate = NO;
    _progressBar.minValue = 0;
    
    _Destination.placeholderString = [NSHomeDirectory() stringByAppendingString:@"/Documents/Samples"];
}

-(NSString*)validateDestination {
    NSString* defaultDestination = [NSHomeDirectory() stringByAppendingString:@"/Documents/Samples"];
    NSString* dropDestination = !([[_Destination stringValue] isEqualToString:@""]) ? [_Destination stringValue] : defaultDestination;
    return (dropDestination);
}

- (IBAction)dropbatTrojan:(id)sender {
    int numberOfSamples = ([_samplesNumber intValue]  > 1) ? [_samplesNumber intValue] : 1;
    NSString* destination = self.validateDestination;
    _progressBar.doubleValue = 0;
    _progressBar.maxValue = 100.f;
    double incrementBy = 100.f / (double)numberOfSamples;
    
    dispatch_queue_t thread = dispatch_queue_create(@"drop sample", nil);
    dispatch_async(thread, ^{
        for (int i=0; i<numberOfSamples; i++) {
            [Samples dropBatTrojan:destination];
           
            dispatch_sync(dispatch_get_main_queue(), ^{
                self->_totalCount++;
                self->_samplesDropped.stringValue = [NSString stringWithFormat:@"%d", self->_totalCount];
                [self->_progressBar incrementBy:incrementBy];
            });
        }
    });
}

- (IBAction)dropDialer:(id)sender {
    int numberOfSamples = [[_samplesNumber stringValue] intValue] > 1 ? [[_samplesNumber stringValue] intValue] : 1;
    NSString* destination = self.validateDestination;
    _progressBar.doubleValue = 0;
    _progressBar.maxValue = 100.f;
    double incrementBy = 100.f / (double)numberOfSamples;
    
    dispatch_queue_t thread = dispatch_queue_create(@"drop sample", nil);
    dispatch_async(thread, ^{
        for (int i=0; i<numberOfSamples; i++) {
            [Samples dropDialer:destination];
            
            dispatch_sync(dispatch_get_main_queue(), ^{
                self->_totalCount++;
                self->_samplesDropped.stringValue = [NSString stringWithFormat:@"%d", self->_totalCount];
                [self->_progressBar incrementBy:incrementBy];
            });
        }
    });
}

- (IBAction)dropEicar:(id)sender {
    int numberOfSamples = [[_samplesNumber stringValue] intValue] > 1 ? [[_samplesNumber stringValue] intValue] : 1;
    NSString* destination = self.validateDestination;
    _progressBar.doubleValue = 0;
    _progressBar.maxValue = 100.f;
    double incrementBy = 100.f / (double)numberOfSamples;
    
    dispatch_queue_t thread = dispatch_queue_create(@"drop sample", nil);
    dispatch_async(thread, ^{
        for (int i=0; i<numberOfSamples; i++) {
            [Samples dropEicar:destination];
            
            dispatch_sync(dispatch_get_main_queue(), ^{
                self->_totalCount++;
                self->_samplesDropped.stringValue = [NSString stringWithFormat:@"%d", self->_totalCount];
                [self->_progressBar incrementBy:incrementBy];
            });
        }
    });
}

- (IBAction)dropCleanable:(id)sender {
    int numberOfSamples = [[_samplesNumber stringValue] intValue] > 1 ? [[_samplesNumber stringValue] intValue] : 1;
    NSString* destination = self.validateDestination;
    _progressBar.doubleValue = 0;
    _progressBar.maxValue = 100.f;
    double incrementBy = 100.f / (double)numberOfSamples;
    
    dispatch_queue_t thread = dispatch_queue_create(@"drop sample", nil);
    dispatch_async(thread, ^{
        for (int i=0; i<numberOfSamples; i++) {
            [Samples dropCleanable:destination];
            
            dispatch_sync(dispatch_get_main_queue(), ^{
                self->_totalCount++;
                self->_samplesDropped.stringValue = [NSString stringWithFormat:@"%d", self->_totalCount];
                [self->_progressBar incrementBy:incrementBy];
            });
        }
    });
}

- (IBAction)dropKeylogger:(id)sender {
    int numberOfSamples = [[_samplesNumber stringValue] intValue] > 1 ? [[_samplesNumber stringValue] intValue] : 1;
    NSString* destination = self.validateDestination;
    _progressBar.doubleValue = 0;
    _progressBar.maxValue = 100.f;
    double incrementBy = 100.f / (double)numberOfSamples;
    
    dispatch_queue_t thread = dispatch_queue_create(@"drop sample", nil);
    dispatch_async(thread, ^{
        for (int i=0; i<numberOfSamples; i++) {
            [Samples dropKeylogger:destination];
            
            dispatch_sync(dispatch_get_main_queue(), ^{
                self->_totalCount++;
                self->_samplesDropped.stringValue = [NSString stringWithFormat:@"%d", self->_totalCount];
                [self->_progressBar incrementBy:incrementBy];
            });
        }
    });
}

- (IBAction)dropSmartdb:(id)sender {
    int numberOfSamples = [[_samplesNumber stringValue] intValue] > 1 ? [[_samplesNumber stringValue] intValue] : 1;
    NSString* destination = self.validateDestination;
    _progressBar.doubleValue = 0;
    _progressBar.maxValue = 100.f;
    double incrementBy = 100.f / (double)numberOfSamples;
    
    dispatch_queue_t thread = dispatch_queue_create(@"drop sample", nil);
    dispatch_async(thread, ^{
        for (int i=0; i<numberOfSamples; i++) {
            [Samples dropSmartdb:destination];
            
            dispatch_sync(dispatch_get_main_queue(), ^{
                self->_totalCount++;
                self->_samplesDropped.stringValue = [NSString stringWithFormat:@"%d", self->_totalCount];
                [self->_progressBar incrementBy:incrementBy];
            });
        }
    });
}

- (IBAction)dropPacked:(id)sender {
    int numberOfSamples = [[_samplesNumber stringValue] intValue] > 1 ? [[_samplesNumber stringValue] intValue] : 1;
    NSString* destination = self.validateDestination;
    _progressBar.doubleValue = 0;
    _progressBar.maxValue = 100.f;
    double incrementBy = 100.f / (double)numberOfSamples;
    
    dispatch_queue_t thread = dispatch_queue_create(@"drop sample", nil);
    dispatch_async(thread, ^{
        for (int i=0; i<numberOfSamples; i++) {
            [Samples dropPacked:destination];
            
            dispatch_sync(dispatch_get_main_queue(), ^{
                self->_totalCount++;
                self->_samplesDropped.stringValue = [NSString stringWithFormat:@"%d", self->_totalCount];
                [self->_progressBar incrementBy:incrementBy];
            });
        }
    });
}

- (IBAction)dropPUA:(id)sender {
    int numberOfSamples = [[_samplesNumber stringValue] intValue] > 1 ? [[_samplesNumber stringValue] intValue] : 1;
    NSString* destination = self.validateDestination;
    _progressBar.doubleValue = 0;
    _progressBar.maxValue = 100.f;
    double incrementBy = 100.f / (double)numberOfSamples;
    
    dispatch_queue_t thread = dispatch_queue_create(@"drop sample", nil);
    dispatch_async(thread, ^{
        for (int i=0; i<numberOfSamples; i++) {
            [Samples dropPUA:destination];
            
            dispatch_sync(dispatch_get_main_queue(), ^{
                self->_totalCount++;
                self->_samplesDropped.stringValue = [NSString stringWithFormat:@"%d", self->_totalCount];
                [self->_progressBar incrementBy:incrementBy];
            });
        }
    });
}

- (IBAction)dropAdware:(id)sender {
    int numberOfSamples = [[_samplesNumber stringValue] intValue] > 1 ? [[_samplesNumber stringValue] intValue] : 1;
    NSString* destination = self.validateDestination;
    _progressBar.doubleValue = 0;
    _progressBar.maxValue = 100.f;
    double incrementBy = 100.f / (double)numberOfSamples;
    
    dispatch_queue_t thread = dispatch_queue_create(@"drop sample", nil);
    dispatch_async(thread, ^{
        for (int i=0; i<numberOfSamples; i++) {
            [Samples dropAdware:destination];
            
            dispatch_sync(dispatch_get_main_queue(), ^{
                self->_totalCount++;
                self->_samplesDropped.stringValue = [NSString stringWithFormat:@"%d", self->_totalCount];
                [self->_progressBar incrementBy:incrementBy];
            });
        }
    });
}

- (IBAction)dropSpyware:(id)sender {
    int numberOfSamples = [[_samplesNumber stringValue] intValue] > 1 ? [[_samplesNumber stringValue] intValue] : 1;
    NSString* destination = self.validateDestination;
    _progressBar.doubleValue = 0;
    _progressBar.maxValue = 100.f;
    double incrementBy = 100.f / (double)numberOfSamples;
    
    dispatch_queue_t thread = dispatch_queue_create(@"drop sample", nil);
    dispatch_async(thread, ^{
        for (int i=0; i<numberOfSamples; i++) {
            [Samples dropSpyware:destination];
            
            dispatch_sync(dispatch_get_main_queue(), ^{
                self->_totalCount++;
                self->_samplesDropped.stringValue = [NSString stringWithFormat:@"%d", self->_totalCount];
                [self->_progressBar incrementBy:incrementBy];
            });
        }
    });
}

- (IBAction)dropApplication:(id)sender {
    int numberOfSamples = [[_samplesNumber stringValue] intValue] > 1 ? [[_samplesNumber stringValue] intValue] : 1;
    NSString* destination = self.validateDestination;
    _progressBar.doubleValue = 0;
    _progressBar.maxValue = 100.f;
    double incrementBy = 100.f / (double)numberOfSamples;
    
    dispatch_queue_t thread = dispatch_queue_create(@"drop sample", nil);
    dispatch_async(thread, ^{
        for (int i=0; i<numberOfSamples; i++) {
            [Samples dropApplication:destination];
            
            dispatch_sync(dispatch_get_main_queue(), ^{
                self->_totalCount++;
                self->_samplesDropped.stringValue = [NSString stringWithFormat:@"%d", self->_totalCount];
                [self->_progressBar incrementBy:incrementBy];
            });
        }
    });
}

- (IBAction)dropSuspected:(id)sender {
    int numberOfSamples = [[_samplesNumber stringValue] intValue] > 1 ? [[_samplesNumber stringValue] intValue] : 1;
    NSString* destination = self.validateDestination;
    _progressBar.doubleValue = 0;
    _progressBar.maxValue = 100.f;
    double incrementBy = 100.f / (double)numberOfSamples;
    
    dispatch_queue_t thread = dispatch_queue_create(@"drop sample", nil);
    dispatch_async(thread, ^{
        for (int i=0; i<numberOfSamples; i++) {
            [Samples dropSuspected:destination];
            
            dispatch_sync(dispatch_get_main_queue(), ^{
                self->_totalCount++;
                self->_samplesDropped.stringValue = [NSString stringWithFormat:@"%d", self->_totalCount];
                [self->_progressBar incrementBy:incrementBy];
            });
        }
    });
}

- (IBAction)dropSignedSuspected:(id)sender {
    int numberOfSamples = [[_samplesNumber stringValue] intValue] > 1 ? [[_samplesNumber stringValue] intValue] : 1;
    NSString* destination = self.validateDestination;
    _progressBar.doubleValue = 0;
    _progressBar.maxValue = 100.f;
    double incrementBy = 100.f / (double)numberOfSamples;
    
    dispatch_queue_t thread = dispatch_queue_create(@"drop sample", nil);
    dispatch_async(thread, ^{
        for (int i=0; i<numberOfSamples; i++) {
            [Samples dropSignedSuspected:destination];
            
            dispatch_sync(dispatch_get_main_queue(), ^{
                self->_totalCount++;
                self->_samplesDropped.stringValue = [NSString stringWithFormat:@"%d", self->_totalCount];
                [self->_progressBar incrementBy:incrementBy];
            });
        }
    });
}

- (IBAction)dropSignedInfected:(id)sender {
    int numberOfSamples = [[_samplesNumber stringValue] intValue] > 1 ? [[_samplesNumber stringValue] intValue] : 1;
    NSString* destination = self.validateDestination;
    _progressBar.doubleValue = 0;
    _progressBar.maxValue = 100.f;
    double incrementBy = 100.f / (double)numberOfSamples;
    
    dispatch_queue_t thread = dispatch_queue_create(@"drop sample", nil);
    dispatch_async(thread, ^{
        for (int i=0; i<numberOfSamples; i++) {
            [Samples dropSignedInfected:destination];
            
            dispatch_sync(dispatch_get_main_queue(), ^{
                self->_totalCount++;
                self->_samplesDropped.stringValue = [NSString stringWithFormat:@"%d", self->_totalCount];
                [self->_progressBar incrementBy:incrementBy];
            });
        }
    });
}

- (IBAction)dropMalwareEDR:(id)sender {
    int numberOfSamples = [[_samplesNumber stringValue] intValue] > 1 ? [[_samplesNumber stringValue] intValue] : 1;
    NSString* destination = self.validateDestination;
    _progressBar.doubleValue = 0;
    _progressBar.maxValue = 100.f;
    double incrementBy = 100.f / (double)numberOfSamples;
    
    dispatch_queue_t thread = dispatch_queue_create(@"drop sample", nil);
    dispatch_async(thread, ^{
        for (int i=0; i<numberOfSamples; i++) {
            [Samples dropMalwareEDR:destination];
            
            dispatch_sync(dispatch_get_main_queue(), ^{
                self->_totalCount++;
                self->_samplesDropped.stringValue = [NSString stringWithFormat:@"%d", self->_totalCount];
                [self->_progressBar incrementBy:incrementBy];
            });
        }
    });
}

- (IBAction)executeRCAPocEdr:(id)sender {
    int numberOfSamples = [[_samplesNumber stringValue] intValue] > 1 ? [[_samplesNumber stringValue] intValue] : 1;
    NSString* destination = self.validateDestination;
    _progressBar.doubleValue = 0;
    _progressBar.maxValue = 100.f;
    double incrementBy = 100.f / (double)numberOfSamples;

    dispatch_queue_t thread = dispatch_queue_create(@"drop sample", nil);
    dispatch_async(thread, ^{
        for (int i=0; i<numberOfSamples; i++) {
            [Samples executeRCAPocEdr:destination];

            dispatch_sync(dispatch_get_main_queue(), ^{
                self->_totalCount++;
                self->_samplesDropped.stringValue = [NSString stringWithFormat:@"%d", self->_totalCount];
                [self->_progressBar incrementBy:incrementBy];
            });
        }
    });
}

- (IBAction)executePocHttpEDR:(id)sender {
    int numberOfSamples = [[_samplesNumber stringValue] intValue] > 1 ? [[_samplesNumber stringValue] intValue] : 1;
    NSString* destination = self.validateDestination;
    _progressBar.doubleValue = 0;
    _progressBar.maxValue = 100.f;
    double incrementBy = 100.f / (double)numberOfSamples;

    dispatch_queue_t thread = dispatch_queue_create(@"drop sample", nil);
    dispatch_async(thread, ^{
        for (int i=0; i<numberOfSamples; i++) {
            [Samples executePocHttpEdr:destination];

            dispatch_sync(dispatch_get_main_queue(), ^{
                self->_totalCount++;
                self->_samplesDropped.stringValue = [NSString stringWithFormat:@"%d", self->_totalCount];
                [self->_progressBar incrementBy:incrementBy];
            });
        }
    });
}

- (IBAction)executeSudospawnATC:(id)sender {
    int numberOfSamples = [[_samplesNumber stringValue] intValue] > 1 ? [[_samplesNumber stringValue] intValue] : 1;
    NSString* destination = self.validateDestination;
    _progressBar.doubleValue = 0;
    _progressBar.maxValue = 100.f;
    double incrementBy = 100.f / (double)numberOfSamples;

    dispatch_queue_t thread = dispatch_queue_create(@"drop sample", nil);
    dispatch_async(thread, ^{
        for (int i=0; i<numberOfSamples; i++) {
            [Samples executeSudospawnATC:destination];

            dispatch_sync(dispatch_get_main_queue(), ^{
                self->_totalCount++;
                self->_samplesDropped.stringValue = [NSString stringWithFormat:@"%d", self->_totalCount];
                [self->_progressBar incrementBy:incrementBy];
            });
        }
    });
}

- (void)applicationWillTerminate:(NSNotification *)aNotification {
    // Insert code here to tear down your application
    [NSApp terminate:nil];
    [[NSApplication sharedApplication] terminate:self];
}

- (BOOL)applicationShouldTerminateAfterLastWindowClosed:
    (NSApplication *)theApplication {
#pragma unused(theApplication)
    return YES;
}


@end
